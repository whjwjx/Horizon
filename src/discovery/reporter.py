"""Generate discovery reports."""

from datetime import datetime
from pathlib import Path
from typing import List

from .discoverer import SourceRecommendation


class DiscoveryReporter:
    """Generate Markdown reports for discovered sources."""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def generate_report(
        self,
        recommendations: List[SourceRecommendation],
        topics: List[str]
    ) -> str:
        """Generate a Markdown report."""

        # Header
        report = self._generate_header(topics)

        # Group by topic
        by_topic = self._group_by_topic(recommendations)

        # Generate sections
        for topic in topics:
            sources = by_topic.get(topic, [])
            if sources:
                report += self._generate_topic_section(topic, sources)

        # Summary
        report += self._generate_summary(recommendations)

        # Quick actions
        report += self._generate_quick_actions(recommendations)

        return report

    def _generate_header(self, topics: List[str]) -> str:
        """Generate report header."""
        date = datetime.now().strftime("%Y-%m-%d")

        return f"""# 🔍 RSS 源发现报告

**日期**: {date}
**搜索话题**: {', '.join(topics)}

---

"""

    def _group_by_topic(self, recommendations: List[SourceRecommendation]) -> dict:
        """Group recommendations by topic."""
        grouped = {}
        for rec in recommendations:
            if rec.topic not in grouped:
                grouped[rec.topic] = []
            grouped[rec.topic].append(rec)
        return grouped

    def _generate_topic_section(self, topic: str, sources: List[SourceRecommendation]) -> str:
        """Generate section for a topic."""
        section = f"## {topic}\n\n"

        for i, source in enumerate(sources, 1):
            stars = "⭐" * min(int(source.quality_score / 2), 5)
            recommendation = "✅ 强烈推荐" if source.quality_score >= 9.0 else "⚠️ 可选"

            section += f"""### {i}. {source.name} {stars}

- **网站**: {source.url}
- **RSS**: `{source.rss_url}`
- **推荐理由**: {source.reason}
- **最近文章**: {', '.join(source.recent_posts[:3])}
- **质量评分**: {source.quality_score:.1f}/10
- **更新频率**: {source.update_frequency}
- **订阅建议**: {recommendation}

"""

        return section

    def _generate_summary(self, recommendations: List[SourceRecommendation]) -> str:
        """Generate summary section."""
        high_quality = sum(1 for r in recommendations if r.quality_score >= 9.0)
        recommended = sum(1 for r in recommendations if r.quality_score >= 8.0)

        return f"""---

## 📊 推荐统计

- **总发现**: {len(recommendations)} 个新源
- **高质量**: {high_quality} 个（评分 ≥ 9.0）
- **建议订阅**: {recommended} 个（评分 ≥ 8.0）

"""

    def _generate_quick_actions(self, recommendations: List[SourceRecommendation]) -> str:
        """Generate quick action section."""
        high_quality = [r for r in recommendations if r.quality_score >= 9.0]

        section = """## 🔧 快速操作

### 添加到配置文件

将以下内容添加到 `data/config.json` 的 `rss` 数组中：

```json
"""

        for source in high_quality[:3]:  # Top 3 recommendations
            section += f"""{{
  "name": "{source.name}",
  "url": "{source.rss_url}",
  "enabled": true,
  "category": "{source.topic}"
}},
"""

        section += """```

### 或使用命令行

```bash
# 查看完整报告
cat data/discovery-report-DATE.md

# 手动添加到配置文件
# 编辑 data/config.json
```

"""

        return section

    def save_report(self, report: str, filename: str = None) -> Path:
        """Save report to file."""
        if not filename:
            date = datetime.now().strftime("%Y-%m-%d")
            filename = f"discovery-report-{date}.md"

        filepath = self.data_dir / filename
        filepath.write_text(report, encoding="utf-8")

        return filepath
