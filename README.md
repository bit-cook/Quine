# Quine - 自复制程序的艺术

[English Documentation](README_EN.md)

> "A quine is a computer program which takes no input and produces a copy of its own source code as its only output."
>
> "Quine 是一个不接受任何输入，唯一的任务就是输出其源代码本身的计算机程序。"

## 📚 项目简介

**Quine**（自产生程序）这一概念源自计算机科学理论，以美国哲学家和逻辑学家 **Willard Van Orman Quine** (1908–2000) 命名。该术语由 Douglas Hofstadter 在其著作《哥德尔、埃舍尔、巴赫》中首次提出。

本项目致力于深入探索 Quine 的各种实现方式、变体形式以及背后的计算理论，从最基础的 Python 实现到复杂的多语言衔尾蛇（Ouroboros）链。

## 🎯 核心原理

Quine 的存在并非巧合，而是**克莱尼递归定理 (Kleene's Recursion Theorem)** 的直接推论。该定理（也称为不动点定理）证明了在任何图灵完备的编程语言中，都存在一个程序可以输出其自身的源代码。

一个典型的 Quine 通常包含两个核心部分：
1.  **代码部分 (Code)**：包含程序的逻辑指令。
2.  **数据部分 (Data)**：包含代码部分的文本表示（通常是字符串形式）。

程序的执行逻辑往往是：**使用数据部分来重构并输出代码部分，同时输出数据部分本身。**

## 🚀 快速开始

### 1. 验证经典 Quine

最直接验证 Quine 的方法是将输出重定向并与源文件比对。

```bash
# 标准 Python 3 实现
python3 classic/quine.py | diff - classic/quine.py

# 极简版本 (29 字符)
python3 classic/quine_short.py | diff - classic/quine_short.py

# 如果 diff 没有输出，说明源文件与输出完全一致，验证成功！
```

### 2. 运行综合演示

我们提供了一个演示脚本，可以自动运行并验证多种类型的 Quine：

```bash
python3 demo.py
```

### 3. 体验增强版特性

本项目还探索了现代工程视角下的 Quine（引入配置与插件）：

```bash
python3 enhanced_quine.py
```

## ✨ 功能特性

本项目不仅仅是代码的堆砌，更是一个完整的 Quine 研究实验室：

*   **多语言支持**: 涵盖 Python, C, Go, Java, Rust, JavaScript 等主流语言的经典实现。
*   **变体探索**: 包含迭代 Quine (A->B->A)、衔尾蛇链、多语言混合 (Polyglot) 等高级形式。
*   **工程化实验**: 尝试将配置管理 (`config.json`) 和插件机制 (`plugins/`) 引入 Quine 设计（见 `enhanced_quine.py`）。
*   **质量保证**: 拥有完整的单元测试 (`tests_new/`) 和 CI/CD 流水线，确保代码的严格自指性。

## 📁 文档索引

为了帮助您更好地理解 Quine，我们整理了详尽的文档：

| 文档 | 说明 |
|------|------|
| [THEORY.md](THEORY.md) | **理论基础**：深入解析不动点定理与 Quine 的数学原理 |
| [EXAMPLES.md](EXAMPLES.md) | **实例解析**：各种语言和形式的 Quine 代码详解 |
| [CHALLENGES.md](CHALLENGES.md) | **编程挑战**：25 个不同难度的 Quine 编写任务 |
| [FAQ.md](FAQ.md) | **常见问题**：关于 Quine 的定义、边界与技巧 |
| [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) | **项目摘要**：项目结构与内容的完整概览 |

## 📂 项目结构

```
Quine/
├── README.md               # 中文主文档
├── README_EN.md            # English Documentation
├── demo.py                 # 综合演示脚本
├── enhanced_quine.py       # 增强版特性演示
├── config.json             # 配置文件
├── classic/                # 经典实现 (Python, C, etc.)
├── variants/               # 变体形式 (迭代、衔尾蛇等)
├── generators/             # Quine 生成器
├── artistic/               # 艺术性 Quine (ASCII, 二维码等)
├── esoteric/               # 难解语言 Quine (Brainfuck 等)
├── plugins/                # 插件系统实验
├── tests_new/              # 自动化测试套件
└── tools/                  # 辅助工具 (验证器、优化器)
```

## 🎯 核心原理

Quine 的实现基于**不动点定理**（Kleene's Recursion Theorem）。一个典型的 Quine 包含两个部分：

1. **数据部分**：存储程序的代码表示
2. **代码部分**：将数据解码并输出

经典结构模式：
```
程序 = 数据 + 使用数据输出 "数据 + 使用数据输出"
```

## 📖 经典示例

### Python 3 极简 Quine (29 字符)

```python
_='_=%r;print(_%%_)';print(_%_)
```

### Python 3 带注释版本

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 3 Quine
"""
s='s=%r;print(s%%s)';print(s%s)
```

### Python 2/3 兼容版本

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
s="s=%r;print(s%%s)"
print(s%s)
```

## 🐍 Python 版本说明

### Python 3 (推荐)

- **位置**: `classic/`, `generators/`, `tests/`, `tools/`, `variants/`, `artistic/`
- **特性**: 类型注解、f-strings、现代语法
- **使用方法**: `python3 <file>`

### Python 2.7 (兼容)

- **位置**: `python2/`
- **说明**: Python 2 已于 2020 年停止维护，仅用于兼容性
- **使用方法**: `python python2/<file>`

## 🎨 变体类型

### 1. 迭代 Quine (Iterative Quine)
程序 A 输出 B，B 输出 C，C 输出 A，形成一个循环。

### 2. 多语言 Quine (Multiquine)
同一个源文件可以被多种编程语言正确解释。

### 3. 衔尾蛇 (Ouroboros)
程序 A 输出程序 B 的源代码，B 输出 C 的源代码...最终 Z 输出 A 的源代码。

## 🧪 编程挑战

1. **最短 Quine**：用最少的字符实现
2. **迭代 Quine**：创建 2+ 循环
3. **多语言 Quine**：同一文件多语言运行
4. **抗辐射 Quine**：容错版本

完整挑战列表见 `CHALLENGES.md`。

## 📝 文档索引

| 文件 | 内容 |
|------|------|
| README.md | 项目介绍与快速开始 |
| THEORY.md | Kleene 不动点定理等理论分析 |
| EXAMPLES.md | 各种 Quine 示例与解析 |
| CHALLENGES.md | 25 个编程挑战 |
| FAQ.md | 常见问题解答 |
| PROJECT_SUMMARY.md | 项目完整摘要 |
| FIXES_REPORT.md | 修复报告 |
| python2/README.md | Python 2 版本说明 |

## 🔗 相关资源

- [Wikipedia - Quine](https://en.wikipedia.org/wiki/Quine_(computing))
- [Rosetta Code - Quine](https://rosettacode.org/wiki/Quine)

## 📝 许可证

MIT License

---

> "Yields falsehood when preceded by its quotation" yields falsehood when preceded by its quotation.
>
> -- Quine's Paradox
