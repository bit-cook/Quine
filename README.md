# Quine - 自复制程序的艺术

[English Documentation](README_EN.md)

> **Quine** 是一种无需外部输入、在运行中完整重构自身源代码的自复制程序。它是计算理论中“不动点”的直观体现，展示了代码如何像生物一样自我繁衍。

## 📚 项目简介

**Quine**（自产生程序）这一概念源自计算机科学理论，以美国哲学家和逻辑学家 **Willard Van Orman Quine** (1908–2000) 命名。该术语由 Douglas Hofstadter 在其著作《哥德尔、埃舍尔、巴赫》中首次提出。

本项目致力于深入探索 Quine 的各种实现方式、变体形式以及背后的计算理论，从最基础的 Python 实现到复杂的多语言衔尾蛇（Ouroboros）链。

本项目 Quine 是一个面向“自复制程序”的深度实验项目，它试图把抽象的 Kleene 不动点定理和自指悖论，落到一整套可运行、可验证、可视化的代码与文档上。本项目从最经典的 Python 极简 Quine 起步，系统收集了多语言实现（Python/C/Go/Java/Rust/JavaScript）、迭代 Quine、Polyglot Multiquine，以及多节点衔尾蛇（Ouroboros）链等变体形式，并提供自动验证器和链生成器，让你可以一键构造并检查任意长度的闭环自复制结构。配合分级教学的 EXAMPLES、理论向的 THEORY、挑战导向的 CHALLENGES，以及一系列工具与演示脚本，这个项目更像是一间“小型自复制程序研究室”，帮助你从直观代码、形式化理论和工程实践三个维度，真正吃透 Quine 的世界。


## 🎯 核心原理

Quine 的存在并非巧合，而是**克莱尼递归定理 (Kleene's Recursion Theorem)** 的直接推论。该定理（也称为不动点定理）证明了在任何图灵完备的编程语言中，都存在一个程序可以输出其自身的源代码。

一个典型的 Quine 通常包含两个核心部分：
1.  **代码部分 (Code)**：包含程序的逻辑指令。
2.  **数据部分 (Data)**：包含代码部分的文本表示（通常是字符串形式）。

程序的执行逻辑往往是：**使用数据部分来重构并输出代码部分，同时输出数据部分本身。**

经典结构模式：
```text
程序 = 数据 + 使用数据输出 "数据 + 使用数据输出"
```

## 📖 经典示例

### Python 3 极简 Quine (29 字符)

```python
_='_=%r;print(_%%_)';print(_%_)
```

### Python 3 标准版 (带注释)

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

## 🚀 快速开始

### 1. 验证 Quine

最直接验证 Quine 的方法是将输出重定向并与源文件比对。

```bash
# 标准 Python 3 实现
python3 classic/quine.py | diff - classic/quine.py

# 极简版本
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

## 🗺️ 学习路线图

本仓库内容丰富，建议按照以下路径循序渐进：

1.  **👀以此为始 (Level 0)**:
    *   运行 `python3 demo.py`，直观感受什么是“程序打印自己”。
    *   阅读本 README 的“核心原理”部分。

2.  **👶 初学乍练 (Level 1)**:
    *   阅读 [EXAMPLES.md](EXAMPLES.md) 中的“Level 1”和“Level 2”，理解 Quine 的基本构造（Code + Data）。
    *   尝试运行 `classic/quine.py` 并修改它，看看会发生什么。

3.  **🧑‍💻 登堂入室 (Level 2)**:
    *   阅读 [THEORY.md](THEORY.md) 了解 Kleene 不动点定理。
    *   完成 [CHALLENGES.md](CHALLENGES.md) 中的前 3 个挑战。
    *   体验 `variants/iterative_quine.py`（A→B→A 循环）。

4.  **🚀 炉火纯青 (Level 3)**:
    *   探索 `variants/ouroboros/`，使用生成器创建自己的 N 节点自指链。
    *   研究 `variants/multiquine.py`，理解多语言共存的技巧。
    *   使用 `tools/` 里的验证器和可视化工具辅助研究。

## ✨ 功能特性

本项目不仅仅是代码的堆砌，更是一个完整的 Quine 研究实验室：

*   **多语言支持**: 涵盖 Python, C, Go, Java, Rust, JavaScript 等主流语言的经典实现。
*   **变体探索**: 包含迭代 Quine (A->B->A)、衔尾蛇链、多语言混合 (Polyglot) 等高级形式。
*   **工程化实验**: 尝试将配置管理 (`config.json`) 和插件机制 (`plugins/`) 引入 Quine 设计（见 `enhanced_quine.py`）。
*   **质量保证**: 拥有完整的单元测试 (`tests_new/`) 和 CI/CD 流水线，确保代码的严格自指性。

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

## 🔬 高级玩法：Ouroboros 链实验套件

本仓库提供了一套围绕衔尾蛇链的高级工具，方便你从“概念”走到“可验证的实验”：

- **生成任意长度的 Python 链**  
  使用生成器在 `variants/ouroboros/` 下创建 N 节点闭环：

  ```bash
  # 生成 3 节点链：py_chain_0.py, py_chain_1.py, py_chain_2.py
  python variants/ouroboros/make_py_chain.py 3
  ```

- **自动验证闭环性质**  
  使用验证器检查“每个节点是否输出下一个节点的源码”：

  ```bash
  python tools/ouroboros_validator.py
  ```

- **可视化链结构**  
  文本 & Graphviz 视图帮助直观看到链路：

  ```bash
  python tools/ouroboros_visualizer.py
  ```

  可以将输出的 DOT 保存为文件，用 Graphviz 渲染为图片。

理论背景与更详细的实例解释，见：

- `EXAMPLES.md` 中的「Level 5：Ouroboros 链」与高级实战部分  
- `THEORY.md` 中的「5.3 Ouroboros 链与多步不动点」

## 🧪 编程挑战

1. **最短 Quine**：用最少的字符实现
2. **迭代 Quine**：创建 2+ 循环
3. **多语言 Quine**：同一文件多语言运行
4. **抗辐射 Quine**：容错版本

完整挑战列表见 `CHALLENGES.md`。

## 📝 文档索引

为了帮助您更好地理解 Quine，我们整理了详尽的文档：

| 文档 | 说明 |
|------|------|
| [THEORY.md](THEORY.md) | **理论基础**：深入解析不动点定理与 Quine 的数学原理 |
| [EXAMPLES.md](EXAMPLES.md) | **实例解析**：各种语言和形式的 Quine 代码详解 |
| [CHALLENGES.md](CHALLENGES.md) | **编程挑战**：25 个不同难度的 Quine 编写任务 |
| [FAQ.md](FAQ.md) | **常见问题**：关于 Quine 的定义、边界与技巧 |
| [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) | **项目摘要**：项目结构与内容的完整概览 |
| [FIXES_REPORT.md](FIXES_REPORT.md) | **修复报告**：历史问题修复记录 |

## 🔗 相关资源

- [Wikipedia - Quine](https://en.wikipedia.org/wiki/Quine_(computing))
- [Rosetta Code - Quine](https://rosettacode.org/wiki/Quine)

## 📝 许可证

MIT License - 自由使用和学习！

---

**GitHub**: https://github.com/bit-cook/Quine

> "Yields falsehood when preceded by its quotation" yields falsehood when preceded by its quotation.
>
> "‘在其引用之后产生谬误’在其引用之后产生谬误。"
>
> -- Quine's Paradox (奎因悖论)
