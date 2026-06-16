"""RSS source discovery using AI and web search."""

import asyncio
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Set
from urllib.parse import urlparse

import httpx
from rich.console import Console
from ddgs import DDGS

from ..ai.client import create_ai_client
from ..models import AIConfig, DiscoveryConfig


@dataclass
class ExistingSources:
    """用户已订阅的信息源"""
    rss_urls: Set[str] = field(default_factory=set)
    subreddits: Set[str] = field(default_factory=set)
    github_repos: Set[str] = field(default_factory=set)
    twitter_users: Set[str] = field(default_factory=set)


@dataclass
class SourceRecommendation:
    """Recommended RSS source."""
    name: str
    url: str
    rss_url: Optional[str]
    topic: str
    quality_score: float
    reason: str
    recent_posts: List[str]
    update_frequency: str
    source_type: str = "rss"  # rss, reddit, github, twitter


class SourceDiscoverer:
    """Discover high-quality RSS sources based on user interests."""

    def __init__(
        self,
        ai_config: AIConfig,
        existing_sources: ExistingSources = None,
        data_dir: str = "data",
        discovery_config: DiscoveryConfig = None
    ):
        self.ai_client = create_ai_client(ai_config)
        self.existing = existing_sources or ExistingSources()
        self.data_dir = Path(data_dir)
        self.console = Console(force_terminal=True)  # Force terminal output
        self.http_client = httpx.AsyncClient(timeout=30.0)
        self.discovery_config = discovery_config or DiscoveryConfig()

    async def discover(self, topics: List[str], max_per_topic: int = 3) -> List[SourceRecommendation]:
        """
        Discover new RSS sources for given topics, excluding already subscribed sources.

        Args:
            topics: List of topics to search for
            max_per_topic: Maximum sources to discover per topic

        Returns:
            List of recommended sources
        """
        all_recommendations = []

        for topic in topics:
            self.console.print(f"\n🔍 Searching for: [cyan]{topic}[/cyan]")
            sys.stdout.flush()

            # Step 1: AI generates search queries
            queries = await self._generate_search_queries(topic)
            self.console.print(f"   Generated {len(queries)} search queries")
            sys.stdout.flush()

            # Step 2: Search web for each query
            for i, query in enumerate(queries, 1):
                self.console.print(f"   🌐 Searching query {i}/{len(queries)}: {query[:50]}...")
                sys.stdout.flush()

                results = await self._web_search(query)
                self.console.print(f"      Found {len(results)} results")
                sys.stdout.flush()

                # Step 3: Extract potential RSS sources
                sources = await self._extract_sources(results, topic)
                self.console.print(f"      Extracted {len(sources)} potential sources")
                sys.stdout.flush()

                # Step 4: Evaluate quality and filter existing
                for source in sources[:max_per_topic]:
                    # Skip if already subscribed
                    if self._is_already_subscribed(source):
                        self.console.print(f"   ⊘ Skipped (already subscribed): {source.get('name', 'Unknown')}")
                        sys.stdout.flush()
                        continue

                    self.console.print(f"   📝 Evaluating: {source.get('name', 'Unknown')[:40]}...")
                    sys.stdout.flush()

                    recommendation = await self._evaluate_source(source, topic)

                    if recommendation and recommendation.quality_score >= self.discovery_config.quality_threshold:
                        all_recommendations.append(recommendation)
                        self.console.print(f"   ✓ Found: {recommendation.name} (Score: {recommendation.quality_score:.1f})")
                    else:
                        score = recommendation.quality_score if recommendation else 0
                        self.console.print(f"   ✗ Low quality (Score: {score:.1f}), skipped")
                    sys.stdout.flush()

        # Sort by quality score
        all_recommendations.sort(key=lambda x: x.quality_score, reverse=True)

        return all_recommendations

    def _is_already_subscribed(self, source: dict) -> bool:
        """Check if source is already subscribed."""
        url = source.get("url", "")
        rss_url = source.get("rss_url", "")

        # Check RSS
        if rss_url and rss_url in self.existing.rss_urls:
            return True
        if url and url in self.existing.rss_urls:
            return True

        # Check Reddit (if URL contains reddit.com)
        if "reddit.com/r/" in url:
            match = re.search(r'reddit\.com/r/([^/]+)', url)
            if match:
                subreddit = match.group(1).lower()
                if subreddit in self.existing.subreddits:
                    return True

        # Check GitHub (if URL contains github.com)
        if "github.com/" in url:
            match = re.search(r'github\.com/([^/]+)/([^/]+)', url)
            if match:
                owner_repo = f"{match.group(1)}/{match.group(2)}".lower()
                if owner_repo in self.existing.github_repos:
                    return True

        return False

    async def _generate_search_queries(self, topic: str) -> List[str]:
        """Generate search queries for a topic using AI."""
        prompt = f"""Generate 3 search queries to find high-quality blogs and RSS feeds about "{topic}".

Requirements:
- Focus on finding blogs, news sites, or publications with RSS feeds
- Use terms like "blog", "RSS feed", "newsletter"
- Prioritize quality over quantity

Return JSON array with 3 search query strings:
["query1", "query2", "query3"]"""

        try:
            response = await self.ai_client.complete(
                system="You are a search expert. Return only valid JSON, no other text.",
                user=prompt
            )

            # Parse JSON response
            json_match = re.search(r'\[.*\]', response, re.DOTALL)
            if json_match:
                queries = json.loads(json_match.group())
                return queries[:3]
        except Exception as e:
            self.console.print(f"   ⚠️  Error generating queries: {e}")

        # Fallback queries
        return [
            f"{topic} blog RSS feed",
            f"best {topic} blogs",
            f"{topic} newsletter RSS"
        ]

    async def _web_search(self, query: str) -> List[dict]:
        """Search the web using DuckDuckGo official library."""
        try:
            # 使用 ddgs 库而不是手动解析 HTML
            with DDGS() as ddgs:
                # 同步搜索，在异步函数中运行
                results = list(ddgs.text(query, max_results=self.discovery_config.search_results_per_query))
            
            formatted_results = []
            for result in results:
                formatted_results.append({
                    "title": result.get("title", ""),
                    "url": result.get("href", ""),
                    "snippet": result.get("body", "")
                })
            
            return formatted_results

        except Exception as e:
            self.console.print(f"   ⚠️  Search error: {e}")
            return []

    async def _extract_sources(self, search_results: List[dict], topic: str) -> List[dict]:
        """Extract potential RSS sources from search results."""
        sources = []

        for result in search_results:
            url = result.get("url", "")
            title = result.get("title", "")

            # Skip obvious non-blog sites
            skip_domains = [
                "youtube.com", "twitter.com", "facebook.com",
                "instagram.com", "linkedin.com", "reddit.com"
            ]

            if any(domain in url for domain in skip_domains):
                continue

            # Try to find RSS feed
            rss_url = await self._find_rss_feed(url)

            if rss_url:
                sources.append({
                    "name": title,
                    "url": url,
                    "rss_url": rss_url,
                    "topic": topic
                })

        return sources

    async def _find_rss_feed(self, website_url: str) -> Optional[str]:
        """Find RSS feed URL for a website."""
        try:
            response = await self.http_client.get(website_url)
            response.raise_for_status()

            html = response.text

            # Common RSS patterns
            rss_patterns = [
                r'<link[^>]*type="application/rss\+xml"[^>]*href="([^"]+)"',
                r'<link[^>]*type="application/atom\+xml"[^>]*href="([^"]+)"',
                r'href="(/feed/)"',
                r'href="(/rss/)"',
                r'href="(/feed\.xml)"',
            ]

            for pattern in rss_patterns:
                match = re.search(pattern, html, re.IGNORECASE)
                if match:
                    rss_url = match.group(1)

                    # Make absolute URL
                    if rss_url.startswith('/'):
                        parsed = urlparse(website_url)
                        rss_url = f"{parsed.scheme}://{parsed.netloc}{rss_url}"

                    return rss_url

            # Try common RSS paths
            common_paths = ["/feed", "/rss", "/feed.xml", "/rss.xml", "/atom.xml"]
            parsed = urlparse(website_url)
            base_url = f"{parsed.scheme}://{parsed.netloc}"

            for path in common_paths:
                test_url = base_url + path
                try:
                    test_response = await self.http_client.head(test_url)
                    if test_response.status_code == 200:
                        return test_url
                except:
                    continue

        except Exception:
            pass

        return None

    async def _evaluate_source(self, source: dict, topic: str) -> Optional[SourceRecommendation]:
        """Evaluate the quality of a potential RSS source."""
        try:
            # Fetch RSS feed
            rss_url = source.get("rss_url")
            if not rss_url:
                return None

            response = await self.http_client.get(rss_url)
            response.raise_for_status()

            # Parse RSS content
            rss_content = response.text

            # Extract recent posts
            recent_posts = self._extract_recent_posts(rss_content)

            if not recent_posts:
                return None

            # AI evaluates quality
            quality_score, reason = await self._ai_evaluate_quality(
                source["name"],
                topic,
                recent_posts,
                rss_content[:500]
            )

            # Estimate update frequency
            update_frequency = self._estimate_update_frequency(rss_content)

            return SourceRecommendation(
                name=source["name"],
                url=source["url"],
                rss_url=rss_url,
                topic=topic,
                quality_score=quality_score,
                reason=reason,
                recent_posts=recent_posts[:3],
                update_frequency=update_frequency
            )

        except Exception as e:
            self.console.print(f"   ⚠️  Error evaluating {source['name']}: {e}")
            return None

    def _extract_recent_posts(self, rss_content: str) -> List[str]:
        """Extract recent post titles from RSS content."""
        posts = []

        # Extract titles
        title_pattern = r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>'
        matches = re.findall(title_pattern, rss_content, re.DOTALL)

        for title in matches[1:6]:  # Skip first (usually feed title)
            title = title.strip()
            if title and len(title) > 10:
                posts.append(title)

        return posts

    async def _ai_evaluate_quality(
        self,
        source_name: str,
        topic: str,
        recent_posts: List[str],
        rss_sample: str
    ) -> tuple[float, str]:
        """Use AI to evaluate source quality."""

        prompt = f"""Evaluate the quality of this RSS source for the topic "{topic}".

Source Name: {source_name}

Recent Posts:
{chr(10).join(f'- {post}' for post in recent_posts)}

RSS Sample:
{rss_sample[:300]}

Evaluate based on 4 dimensions (each 0-2.5 points):

1. Content relevance to the topic (0-2.5 points)
   - 2.5: Highly relevant, focused on the topic
   - 1.5: Moderately relevant
   - 0.5: Tangentially related

2. Content depth and quality (0-2.5 points)
   - 2.5: In-depth, original insights
   - 1.5: Decent coverage
   - 0.5: Shallow or generic

3. Update frequency (0-2.5 points)
   - 2.5: Regular updates (weekly+)
   - 1.5: Occasional updates
   - 0.5: Rarely updated

4. Professional tone (0-2.5 points)
   - 2.5: Expert-level, authoritative
   - 1.5: Professional
   - 0.5: Casual or amateur

Total score = sum of 4 dimensions (0-10)

Scoring guide:
- 8.5+: Excellent source, must subscribe
- 7.0-8.4: Good source, recommended
- 5.5-6.9: Acceptable, consider subscribing
- Below 5.5: Low quality, skip

Return JSON:
{{
  "score": <float between 0-10>,
  "reason_en": "<one sentence explanation in English>",
  "reason_zh": "<one sentence explanation in Chinese>"
}}"""

        try:
            response = await self.ai_client.complete(
                system="You are a content quality evaluator. Return only valid JSON.",
                user=prompt
            )

            # Parse JSON
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                result = json.loads(json_match.group())
                score = float(result.get("score", 0))
                reason_en = result.get("reason_en", "")
                reason_zh = result.get("reason_zh", "")

                # 合并英文和中文理由
                if reason_en and reason_zh:
                    reason = f"{reason_en}\n{reason_zh}"
                elif reason_en:
                    reason = reason_en
                elif reason_zh:
                    reason = reason_zh
                else:
                    reason = "Unable to evaluate quality"

                return score, reason

        except Exception:
            pass

        # Default score
        return 5.0, "Unable to evaluate quality"

    def _estimate_update_frequency(self, rss_content: str) -> str:
        """Estimate how often the source updates."""
        # Simple heuristic based on content length
        if len(rss_content) > 50000:
            return "Multiple times per day"
        elif len(rss_content) > 20000:
            return "Daily"
        elif len(rss_content) > 5000:
            return "Weekly"
        else:
            return "Occasional"

    async def close(self):
        """Close HTTP client."""
        await self.http_client.aclose()
