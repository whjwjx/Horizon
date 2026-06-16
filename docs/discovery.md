# 🔍 RSS 源发现工具

自动发现高质量的 RSS 订阅源，根据你的兴趣推荐新内容。

## 📋 功能特点

- ✅ **AI 驱动搜索**：使用 AI 生成精准的搜索查询
- ✅ **质量评估**：自动评估 RSS 源的质量和相关性
- ✅ **智能推荐**：根据评分推荐最值得订阅的源
- ✅ **详细报告**：生成 Markdown 格式的推荐报告

## 🚀 快速开始

### 基本用法

```bash
# 使用默认话题（从配置文件提取）
uv run horizon-discover

# 指定话题
uv run horizon-discover --topics "AI" "个人成长" "音乐"

# 限制每个话题的发现数量
uv run horizon-discover --topics "AI" --max-per-topic 5
```

### 高级选项

```bash
# 自定义输出文件
uv run horizon-discover --output data/my-discovery.md

# 使用自定义配置文件
uv run horizon-discover --config data/config.json
```

## 📊 输出示例

### 终端输出

```
🔍 RSS 源发现工具
搜索话题: AI, 个人成长, 音乐
每个话题最多发现: 3 个源

🔍 Searching for: AI
   Generated 3 search queries
   ✓ Found: AI Supremacy Blog (Score: 9.2)
   ✓ Found: The AI Times (Score: 8.5)

🔍 Searching for: 个人成长
   Generated 3 search queries
   ✓ Found: Better Thinking (Score: 9.0)

✅ 报告已保存: data/discovery-report-2026-06-16.md

📊 发现统计
┌───────────────┬────────┐
│ 指标          │   数量 │
├───────────────┼────────┤
│ 总发现        │      3 │
│ 高质量 (≥9.0) │      2 │
│ 建议订阅 (≥8.0)│      3 │
└───────────────┴────────┘

🏆 Top 推荐

1. AI Supremacy Blog ⭐⭐⭐⭐⭐
   话题: AI
   评分: 9.2/10
   理由: 深度 AI 分析，高质量内容
   建议: ✅ 强烈推荐
   RSS: https://aisupremacy.com/feed
```

### 报告文件

生成的 Markdown 报告包含：

```markdown
# 🔍 RSS 源发现报告

**日期**: 2026-06-16
**搜索话题**: AI, 个人成长, 音乐

---

## AI

### 1. AI Supremacy Blog ⭐⭐⭐⭐⭐

- **网站**: https://aisupremacy.com
- **RSS**: `https://aisupremacy.com/feed`
- **推荐理由**: 深度 AI 分析，每周更新 2-3 篇高质量文章
- **最近文章**: GPT-5 架构解析, AI Agent 实战指南
- **质量评分**: 9.2/10
- **更新频率**: 每周 2-3 次
- **订阅建议**: ✅ 强烈推荐

---

## 📊 推荐统计

- **总发现**: 3 个新源
- **高质量**: 2 个（评分 ≥ 9.0）
- **建议订阅**: 3 个（评分 ≥ 8.0）

## 🔧 快速操作

### 添加到配置文件

将以下内容添加到 `data/config.json` 的 `rss` 数组中：

```json
{
  "name": "AI Supremacy Blog",
  "url": "https://aisupremacy.com/feed",
  "enabled": true,
  "category": "AI"
},
```
```

## 🎯 使用场景

### 场景 1：每周发现新源

```bash
# 每周一运行，发现新内容
uv run horizon-discover --topics "AI" "编程" "科技"
```

### 场景 2：特定话题深入挖掘

```bash
# 深入挖掘特定话题
uv run horizon-discover --topics "AI Agent" --max-per-topic 5
```

### 场景 3：补充现有订阅

```bash
# 基于现有配置自动发现
uv run horizon-discover
```

## ⚙️ 配置说明

### 话题来源

工具会按以下优先级获取话题：

1. **命令行指定**：`--topics "AI" "音乐"`
2. **配置文件提取**：从现有 RSS 源的 `category` 字段提取
3. **默认话题**：`["AI", "科技", "编程"]`

### 质量评分标准

| 评分 | 说明 | 建议 |
|------|------|------|
| 9.0-10.0 | 高质量，深度内容 | ✅ 强烈推荐 |
| 8.0-8.9 | 质量良好 | ⚠️ 可选 |
| 7.0-7.9 | 质量一般 | 不推荐 |
| < 7.0 | 质量较低 | 不显示 |

### 评估维度

1. **内容相关性**：与话题的匹配程度
2. **内容深度**：文章质量和专业性
3. **更新频率**：发布频率和稳定性
4. **专业程度**：作者专业性和权威性

## 💡 最佳实践

### 1. 定期运行

```bash
# 每周运行一次
# 建议在周末或周一运行
uv run horizon-discover
```

### 2. 审核推荐

- 查看生成的报告
- 阅读推荐理由
- 检查最近文章
- 决定是否订阅

### 3. 手动添加

- 复制报告中的 JSON 配置
- 粘贴到 `data/config.json`
- 运行 `uv run horizon --hours 24` 测试

### 4. 持续优化

- 定期清理低质量源
- 添加新发现的高质量源
- 调整话题和评分阈值

## 🔧 技术实现

### 工作流程

```
1. AI 生成搜索查询
   ↓
2. DuckDuckGo 搜索
   ↓
3. 提取潜在 RSS 源
   ↓
4. 验证 RSS 可用性
   ↓
5. AI 评估质量
   ↓
6. 生成推荐报告
```

### 成本估算

- **每次搜索**：约 1000-2000 tokens
- **质量评估**：约 500-1000 tokens/源
- **总成本**：约 ¥0.02-0.05/次

## 🚨 注意事项

### 1. 搜索限制

- DuckDuckGo 可能限制请求频率
- 建议每周运行 1-2 次
- 避免短时间内多次运行

### 2. RSS 可用性

- 部分网站可能没有 RSS
- RSS 地址可能变化
- 建议定期检查订阅源

### 3. 质量评估

- AI 评估可能不准确
- 建议人工审核推荐
- 根据实际阅读体验调整

## 📝 常见问题

### Q: 为什么没有发现新源？

**A: 可能原因**：
- 话题太窄，搜索结果少
- 搜索引擎限制
- 网络问题

**解决方案**：
- 尝试更广泛的话题
- 等待一段时间后重试
- 检查网络连接

### Q: 如何提高发现质量？

**A: 建议**：
- 使用具体的话题关键词
- 增加 `--max-per-topic` 参数
- 多次运行，积累发现

### Q: 发现的源质量不高怎么办？

**A: 建议**：
- 提高质量阈值（默认 7.0）
- 人工审核推荐
- 手动添加已知高质量源

## 🔗 相关命令

```bash
# 运行 Horizon 生成日报
uv run horizon --hours 24

# 配置向导
uv run horizon-wizard

# Webhook 测试
uv run horizon-webhook --help
```

## 📚 扩展阅读

- [Horizon 配置指南](./docs/configuration.md)
- [RSS 源推荐](./信息源配置指南.md)
- [GitHub 项目](https://github.com/Thysrael/Horizon)

---

**提示**：这是一个实验性功能，建议结合人工审核使用。
