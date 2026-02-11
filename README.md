# Quine - 自复制程序的艺术

[English Documentation](README_EN.md)

> "A quine is a computer program which takes no input and produces a copy of its own source code as its only output."

## 📚 项目简介

Quine（以哲学家 Willard Van Orman Quine 命名）是一个**不接受任何输入**，唯一的任务就是**输出其源代码本身**的计算机程序。
本项目深入探索了 Quine 的各种实现方式、变体形式以及相关的计算理论。

## ✨ 功能特性

*   **多语言支持**: 包含 Python, C, Go, Java, Rust 等多种语言的经典实现。
*   **增强功能**: 新增配置化支持 (`config.json`) 和插件机制 (`plugins/`)。
*   **质量保证**: 包含完整的单元测试 (`tests_new/`) 和 CI/CD 配置。
*   **文档完善**: 提供中英文双语文档。

## 🚀 快速开始

### 验证一个 Quine

```bash
# 标准 Python 3 Quine
python3 classic/quine.py | diff - classic/quine.py

# 极简版本
python3 classic/quine_short.py | diff - classic/quine_short.py
```

### 运行增强版

```bash
python3 enhanced_quine.py
```

## ⚙️ 配置说明

您可以通过 `config.json` 配置输出格式和语言：

```json
{
    "output_format": "text",
    "language": "en",
    "plugins_enabled": true
}
```

## 🛠️ 二次开发指南

项目支持简单的插件机制。在 `plugins/` 目录下创建 Python 脚本并定义钩子函数即可：

```python
def pre_process(code):
    return code
```

## 📝 许可证

MIT License
