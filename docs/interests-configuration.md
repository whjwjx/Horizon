# 📝 用户兴趣配置指南

## 🎯 配置位置

用户兴趣配置在 `data/config.json` 文件中的 `interests` 字段：

```json
{
  "version": "1.0",
  "ai": {
    // AI 配置...
  },
  "interests": [
    "AI",
    "机器学习",
    "个人成长",
    "音乐",
    "健身",
    "艺术审美",
    "思维认知"
  ],
  "sources": {
    // 信息源配置...
  }
}
```

## 📋 配置说明

### 字段格式

```json
"interests": [
  "兴趣1",
  "兴趣2",
  "兴趣3",
  // ... 更多兴趣
]
```

### 配置规则

1. **类型**：字符串数组
2. **必填**：否（有默认值）
3. **默认值**：`["AI", "科技", "编程"]`
4. **数量限制**：建议 3-10 个兴趣
5. **字符限制**：每个兴趣建议不超过 20 个字符

## 🎨 配置示例

### 示例 1：技术爱好者

```json
{
  "interests": [
    "AI",
    "机器学习",
    "编程",
    "Web开发",
    "云计算",
    "开源项目"
  ]
}
```

### 示例 2：个人成长

```json
{
  "interests": [
    "个人成长",
    "习惯养成",
    "思维认知",
    "时间管理",
    "阅读",
    "写作"
  ]
}
```

### 示例 3：多元化兴趣

```json
{
  "interests": [
    "AI",
    "个人成长",
    "音乐",
    "健身",
    "艺术",
    "创业",
    "投资"
  ]
}
```

## 🔧 使用场景

### 场景 1：信息源发现

```bash
# 运行发现工具，自动使用配置的兴趣
uv run horizon-discover

# 输出：
Using interests from config: AI, 机器学习, 个人成长, 音乐, 健身, 艺术审美, 思维认知
```

### 场景 2：临时指定兴趣

```bash
# 临时指定兴趣（覆盖配置文件）
uv run horizon-discover --topics "AI" "音乐"

# 输出：
Using topics from command line: AI, 音乐
```

### 场景 3：不配置兴趣

```json
{
  "interests": []  // 空数组或不配置
}
```

```bash
# 会从 RSS 源的 category 字段提取兴趣
uv run horizon-discover

# 输出：
Using topics from RSS categories: AI, tech-news, growth
```

## 📊 优先级规则

兴趣话题的获取优先级：

1. **命令行指定**（最高优先级）
   ```bash
   uv run horizon-discover --topics "AI" "音乐"
   ```

2. **配置文件 interests 字段**
   ```json
   "interests": ["AI", "音乐"]
   ```

3. **RSS 源的 category 字段**
   ```json
   "rss": [
     {
       "name": "OpenAI Blog",
       "category": "AI"  // ← 提取兴趣
     }
   ]
   ```

4. **默认话题**（最低优先级）
   ```python
   ["AI", "科技", "编程"]
   ```

## 💡 最佳实践

### 1. 兴趣数量

**推荐**：3-7 个兴趣

```json
"interests": [
  "AI",           // 主要兴趣
  "编程",         // 主要兴趣
  "个人成长",     // 次要兴趣
  "音乐"          // 次要兴趣
]
```

**避免**：过多兴趣

```json
// ❌ 不推荐：兴趣太多，发现结果分散
"interests": [
  "AI", "编程", "音乐", "健身", "艺术", "创业",
  "投资", "阅读", "写作", "旅行", "美食", "摄影"
]
```

### 2. 兴趣描述

**推荐**：简洁明确

```json
"interests": [
  "AI",           // ✅ 简洁
  "机器学习",     // ✅ 明确
  "个人成长"      // ✅ 清晰
]
```

**避免**：过于宽泛或模糊

```json
// ❌ 不推荐：过于宽泛
"interests": [
  "科技",         // 太宽泛
  "生活",         // 太模糊
  "学习"          // 不够具体
]
```

### 3. 兴趣分类

建议按重要性分类：

```json
"interests": [
  // 核心兴趣（职业相关）
  "AI",
  "机器学习",
  "编程",

  // 个人兴趣（生活相关）
  "个人成长",
  "音乐",
  "健身",

  // 探索兴趣（尝试新领域）
  "艺术审美",
  "思维认知"
]
```

### 4. 定期更新

建议每月更新一次兴趣配置：

```bash
# 1. 查看当前配置
cat data/config.json | grep -A 10 "interests"

# 2. 编辑配置文件
# 根据最近阅读的内容调整兴趣

# 3. 测试新配置
uv run horizon-discover
```

## 🚀 高级配置

### 1. 动态兴趣

可以根据季节或项目调整兴趣：

```json
// 项目期间
"interests": [
  "AI",
  "编程",
  "项目管理"
]

// 学习期间
"interests": [
  "AI",
  "机器学习",
  "深度学习"
]

// 休闲期间
"interests": [
  "音乐",
  "艺术",
  "旅行"
]
```

### 2. 兴趣权重

虽然当前版本不支持权重，但可以通过顺序暗示重要性：

```json
"interests": [
  "AI",           // 最重要
  "编程",         // 次重要
  "个人成长",     // 一般重要
  "音乐"          // 兴趣爱好
]
```

### 3. 兴趣标签

可以为兴趣添加标签（未来功能）：

```json
"interests": [
  {
    "name": "AI",
    "priority": "high",
    "tags": ["work", "research"]
  },
  {
    "name": "音乐",
    "priority": "low",
    "tags": ["hobby", "relax"]
  }
]
```

## 📝 常见问题

### Q1: 兴趣配置会影响日报内容吗？

**A**: 不会。兴趣配置只影响 `horizon-discover` 命令的搜索范围，不会影响日报的生成内容。日报内容由 `sources` 配置决定。

### Q2: 兴趣可以是中文吗？

**A**: 可以。支持中文、英文、或混合使用。

```json
"interests": [
  "AI",
  "机器学习",
  "Web Development",
  "个人成长"
]
```

### Q3: 兴趣配置后需要重启吗？

**A**: 不需要。配置文件修改后立即生效，下次运行命令时自动读取。

### Q4: 如何查看当前使用的兴趣？

**A**: 运行发现命令时会显示：

```bash
uv run horizon-discover

# 输出：
Using interests from config: AI, 机器学习, 个人成长
```

### Q5: 兴趣可以重复吗？

**A**: 不建议重复。虽然技术上可以重复，但没有意义。

```json
// ❌ 不推荐
"interests": [
  "AI",
  "AI",
  "机器学习"
]

// ✅ 推荐
"interests": [
  "AI",
  "机器学习"
]
```

## 🔗 相关配置

### 与 RSS 源的 category 关系

```json
{
  "interests": ["AI", "个人成长"],

  "sources": {
    "rss": [
      {
        "name": "OpenAI Blog",
        "url": "https://openai.com/blog/rss.xml",
        "category": "AI"  // ← 与兴趣对应
      },
      {
        "name": "James Clear",
        "url": "https://jamesclear.com/feed",
        "category": "growth"  // ← 与兴趣对应
      }
    ]
  }
}
```

### 与发现命令的关系

```bash
# 使用配置的兴趣
uv run horizon-discover

# 临时覆盖配置
uv run horizon-discover --topics "AI" "音乐"

# 查看帮助
uv run horizon-discover --help
```

## 📚 扩展阅读

- [Horizon 配置指南](./docs/configuration.md)
- [信息源配置指南](./信息源配置指南.md)
- [发现功能文档](./docs/discovery.md)

---

**提示**：兴趣配置是发现功能的核心，建议定期调整以获得最佳推荐效果。
