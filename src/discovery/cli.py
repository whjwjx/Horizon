#!/usr/bin/env python3
"""RSS source discovery CLI."""

import asyncio
import sys
import os
from pathlib import Path

# Fix Windows encoding issue
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import click
from rich.console import Console
from rich.table import Table
from dotenv import load_dotenv

# Load .env file
load_dotenv()

from ..models import Config
from ..storage.manager import StorageManager
from .discoverer import SourceDiscoverer, ExistingSources
from .reporter import DiscoveryReporter


console = Console()


def load_existing_sources(config: Config) -> ExistingSources:
    """加载用户已订阅的信息源"""
    existing = ExistingSources()

    # RSS 源
    for rss in config.sources.rss:
        if rss.enabled:
            existing.rss_urls.add(rss.url)

    # Reddit Subreddit
    if config.sources.reddit.enabled:
        for sub in config.sources.reddit.subreddits:
            if sub.enabled:
                existing.subreddits.add(sub.subreddit.lower())

    # GitHub 仓库
    for gh in config.sources.github:
        if gh.enabled:
            owner_repo = f"{gh.owner}/{gh.repo}"
            existing.github_repos.add(owner_repo.lower())

    # Twitter 用户
    if config.sources.twitter and config.sources.twitter.enabled:
        for user in config.sources.twitter.users:
            if user.enabled:
                existing.twitter_users.add(user.username.lower())

    return existing


@click.command()
@click.option(
    '--topics',
    '-t',
    multiple=True,
    help='Topics to search for (e.g., "AI" "个人成长")'
)
@click.option(
    '--max-per-topic',
    '-m',
    default=3,
    help='Maximum sources to discover per topic (default: 3)'
)
@click.option(
    '--output',
    '-o',
    type=click.Path(),
    default='data/discovery-report.md',
    help='Output report file'
)
@click.option(
    '--config',
    '-c',
    type=click.Path(exists=True),
    default='data/config.json',
    help='Config file path'
)
def main(
    topics: tuple,
    max_per_topic: int,
    output: str,
    config: str
):
    """
    Discover high-quality RSS sources based on your interests.

    Example:
        horizon-discover --topics "AI" "个人成长" --max-per-topic 3
    """
    asyncio.run(run_discovery(topics, max_per_topic, output, config))


async def run_discovery(
    topics: tuple,
    max_per_topic: int,
    output: str,
    config_path: str
):
    """Run the discovery process."""

    # Load config
    storage = StorageManager(data_dir=str(Path(config_path).parent))
    try:
        config = storage.load_config()
    except Exception as e:
        console.print(f"[red]❌ Error loading config: {e}[/red]")
        sys.exit(1)

    # Load existing sources
    existing_sources = load_existing_sources(config)

    # Display existing sources
    console.print("\n[bold]📖 已加载现有配置：[/bold]")
    console.print(f"  - RSS: [cyan]{len(existing_sources.rss_urls)}[/cyan] 个已订阅")
    console.print(f"  - Reddit: [cyan]{len(existing_sources.subreddits)}[/cyan] 个已订阅")
    console.print(f"  - GitHub: [cyan]{len(existing_sources.github_repos)}[/cyan] 个已订阅")

    # Use topics from config if not specified
    if not topics:
        # 优先使用 config.interests
        if config.interests:
            topics = config.interests
            console.print(f"\n[cyan]Using interests from config: {', '.join(topics)}[/cyan]")
        else:
            # 备选：从现有 RSS 源的 category 提取
            existing_topics = set()
            for rss in config.sources.rss:
                if rss.category:
                    existing_topics.add(rss.category)

            if existing_topics:
                topics = list(existing_topics)
                console.print(f"\n[cyan]Using topics from RSS categories: {', '.join(topics)}[/cyan]")
            else:
                # 默认话题
                topics = ["AI", "科技", "编程"]
                console.print(f"\n[yellow]No topics specified, using defaults: {', '.join(topics)}[/yellow]")

    console.print(f"\n[bold green]🔍 信息源发现工具[/bold green]")
    console.print(f"[bold]搜索话题:[/bold] {', '.join(topics)}")
    console.print(f"[bold]每个话题最多发现:[/bold] {max_per_topic} 个源")
    console.print(f"[bold]过滤已订阅源:[/bold] ✅ 启用\n")

    # Initialize discoverer with existing sources
    discoverer = SourceDiscoverer(config.ai, existing_sources)

    try:
        # Discover sources
        recommendations = await discoverer.discover(list(topics), max_per_topic)

        if not recommendations:
            console.print("\n[yellow]⚠️  没有发现新的高质量信息源[/yellow]")
            console.print("[yellow]建议：尝试不同的关键词或增加搜索范围[/yellow]")
            console.print(f"[yellow]提示：已过滤 {len(existing_sources.rss_urls) + len(existing_sources.subreddits) + len(existing_sources.github_repos)} 个已订阅源[/yellow]")
            return

        # Generate report
        reporter = DiscoveryReporter()
        report = reporter.generate_report(recommendations, list(topics))

        # Save report
        output_path = reporter.save_report(report, output)
        console.print(f"\n[green]✅ 报告已保存: {output_path}[/green]")

        # Display summary
        display_summary(recommendations, existing_sources)

        # Display top recommendations
        display_top_recommendations(recommendations[:5])

    finally:
        await discoverer.close()


def display_summary(recommendations: list, existing: ExistingSources):
    """Display discovery summary."""
    console.print("\n[bold]📊 发现统计[/bold]")

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("指标", style="cyan")
    table.add_column("数量", justify="right")

    total = len(recommendations)
    high_quality = sum(1 for r in recommendations if r.quality_score >= 9.0)
    recommended = sum(1 for r in recommendations if r.quality_score >= 8.0)
    filtered = len(existing.rss_urls) + len(existing.subreddits) + len(existing.github_repos)

    table.add_row("总发现", str(total))
    table.add_row("高质量 (≥9.0)", str(high_quality))
    table.add_row("建议订阅 (≥8.0)", str(recommended))
    table.add_row("已过滤（已订阅）", str(filtered))

    console.print(table)


def display_top_recommendations(recommendations: list):
    """Display top recommendations."""
    console.print("\n[bold]🏆 Top 推荐[/bold]\n")

    for i, rec in enumerate(recommendations, 1):
        stars = "⭐" * min(int(rec.quality_score / 2), 5)
        recommendation = "✅ 强烈推荐" if rec.quality_score >= 9.0 else "⚠️ 可选"

        console.print(f"[bold]{i}. {rec.name}[/bold] {stars}")
        console.print(f"   [dim]话题:[/dim] {rec.topic}")
        console.print(f"   [dim]评分:[/dim] {rec.quality_score:.1f}/10")
        console.print(f"   [dim]理由:[/dim] {rec.reason}")
        console.print(f"   [dim]建议:[/dim] {recommendation}")
        console.print(f"   [dim]RSS:[/dim] {rec.rss_url}")
        console.print()


if __name__ == '__main__':
    main()
