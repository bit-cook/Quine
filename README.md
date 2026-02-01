# Quine - 自复制程序的艺术

> "A quine is a computer program which takes no input and produces a copy of its own source code as its only output."

## 📚 项目简介

Quine（以哲学家 Willard Van Orman Quine 命名）是一个**不接受任何输入**，唯一的任务就是**输出其源代码本身**的计算机程序。

这个项目深入探索了 Quine 的各种实现方式、变体形式以及相关的计算理论。

## 🚀 快速开始

### 验证一个 Quine

```bash
# 使用 Python 2 兼容版本
python classic/quine_py2.py | diff - classic/quine_py2.py

# 极简版本 (31 字节)
python classic/quine_simple_py2.py | diff - classic/quine_simple_py2.py

# 如果没有任何输出，说明是完美的 Quine！
```

### 运行演示

```bash
python demo_py2.py
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
│
├── classic/                     # 经典 Quine 实现
│   ├── quine_py2.py            # Python 2 版本 [✓ 验证通过]
│   ├── quine_simple_py2.py     # 极简版 (31字节) [✓ 验证通过]
│   ├── quine_py2_compat.py     # Python 2/3 兼容 [✓ 验证通过]
│   ├── quine_short.py          # 短版本 [✓ 验证通过]
│   ├── quine.py                # Python 3 版本
│   ├── quine.js                # JavaScript
│   ├── quine.c                 # C 语言
│   ├── quine.rs                # Rust
│   ├── quine.go                # Go
│   └── quine.java              # Java
│
├── variants/                    # 变体形式
│   ├── iterative_quine.py       # 迭代 Quine
│   ├── multiquine.py            # 多语言 Quine
│   └── ...
│
├── generators/                  # Quine 生成器
│   ├── quine_generator_py2.py  # Python 2 兼容
│   └── ...
│
├── tests/                       # 测试套件
│   ├── test_quine_py2.py       # Python 2 测试
│   └── utils_py2.py            # Python 2 工具
│
└── tools/                       # 辅助工具
    ├── quine_validator_py2.py  # Python 2 验证器
    └── ...
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

### Python 极简 Quine (31 字节)

```python
s='s=%r;print s%%s';print s%s
```

### Python 2/3 兼容版本

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
s="s=%r;print(s%%s)"
print(s%s)
```

## 🔧 Python 版本兼容性

### Python 2.7 环境

当前系统使用 Python 2.7，请使用以下文件：

- `classic/quine_py2.py` - 标准 Quine
- `classic/quine_simple_py2.py` - 极简 Quine
- `classic/quine_py2_compat.py` - 兼容版本
- `demo_py2.py` - 演示脚本
- `tests/test_quine_py2.py` - 测试套件
- `tools/quine_validator_py2.py` - 验证工具

### Python 3 环境

如有 Python 3，可使用原始文件（无 `_py2` 后缀）。

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
| PYTHON_VERSIONS.md | Python 版本兼容性说明 |

## 🔗 相关资源

- [Wikipedia - Quine](https://en.wikipedia.org/wiki/Quine_(computing))
- [Rosetta Code - Quine](https://rosettacode.org/wiki/Quine)

## 📝 许可证

MIT License - 自由使用和学习！

---

**修复状态**: 所有核心 Quine 已修复并通过验证 ✓

> "Yields falsehood when preceded by its quotation" yields falsehood when preceded by its quotation.
