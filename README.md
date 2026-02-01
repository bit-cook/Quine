# Quine - 自复制程序的艺术

> "A quine is a computer program which takes no input and produces a copy of its own source code as its only output."

## 📚 项目简介

Quine（以哲学家 Willard Van Orman Quine 命名）是一个**不接受任何输入**，唯一的任务就是**输出其源代码本身**的计算机程序。

这个项目深入探索了 Quine 的各种实现方式、变体形式以及相关的计算理论。

**🎯 本项目以 Python 3 为主，同时提供 Python 2 兼容版本。**

## 🚀 快速开始

### 验证一个 Quine (Python 3)

```bash
# 标准 Python 3 Quine
python3 classic/quine.py | diff - classic/quine.py

# 极简版本
python3 classic/quine_short.py | diff - classic/quine_short.py

# 如果没有任何输出，说明是完美的 Quine！
```

### 运行演示

```bash
python3 demo.py
```

### Python 2 版本

如需 Python 2 兼容版本：

```bash
python python2/quine_py2.py | diff - python2/quine_py2.py
```

## 📁 项目结构

```
Quine/
├── README.md                    # 本文件
├── THEORY.md                    # 深入的理论分析
├── CHALLENGES.md                # Quine 编程挑战
├── EXAMPLES.md                  # 示例代码
├── FAQ.md                       # 常见问题
├── PROJECT_SUMMARY.md           # 项目摘要
├── FIXES_REPORT.md              # 修复报告
├── demo.py                      # Python 3 演示脚本
│
├── classic/                     # 经典 Quine 实现 (Python 3)
│   ├── quine.py                # 标准 Quine
│   ├── quine_short.py          # 极简版
│   ├── quine.js                # JavaScript
│   ├── quine.c                 # C 语言
│   ├── quine.rs                # Rust
│   ├── quine.go                # Go
│   └── quine.java              # Java
│
├── python2/                     # Python 2.7 兼容版本
│   ├── README.md               # Python 2 说明
│   ├── quine_py2.py            # Python 2 Quine
│   ├── quine_py2_compat.py     # Python 2/3 兼容
│   ├── quine_simple_py2.py     # 极简版
│   ├── quine_generator_py2.py  # 生成器
│   ├── quine_validator_py2.py  # 验证工具
│   ├── test_quine_py2.py       # 测试套件
│   └── demo_py2.py             # 演示脚本
│
├── variants/                    # 变体形式 (Python 3)
│   ├── iterative_quine.py       # 迭代 Quine
│   ├── multiquine.py            # 多语言 Quine
│   ├── ouroboros/               # 衔尾蛇链
│   └── ...
│
├── generators/                  # Quine 生成器 (Python 3)
│   ├── quine_generator.py       # 通用生成器
│   ├── meta_quine.py            # 元生成器
│   └── polyglot_generator.py    # 多语言生成器
│
├── artistic/                    # 艺术性 Quine (Python 3)
│   ├── ascii_art_quine.py       # ASCII 艺术
│   ├── game_of_life_quine.py    # 生命游戏
│   ├── musical_quine.py         # 音乐 Quine
│   └── qr_quine.py              # 二维码 Quine
│
├── tests/                       # 测试套件 (Python 3)
│   ├── test_quine.py            # 主测试
│   └── utils.py                 # 工具函数
│
└── tools/                       # 辅助工具 (Python 3)
    ├── quine_validator.py       # 验证器
    ├── size_optimizer.py        # 大小优化器
    └── visualizer.py            # 可视化工具
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

MIT License - 自由使用和学习！

---

**GitHub**: https://github.com/bit-cook/Quine

> "Yields falsehood when preceded by its quotation" yields falsehood when preceded by its quotation.
