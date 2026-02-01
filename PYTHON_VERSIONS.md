# Python 版本兼容性说明

## 概述

本项目主要使用 **Python 3** 语法编写，但提供了一些 Python 2 兼容版本。

## Python 版本要求

### Python 3 版本（推荐）
- 需要 Python 3.6+
- 使用类型注解、f-strings 等新特性
- 文件位置: 大部分 `.py` 文件

### Python 2 兼容版本
- 兼容 Python 2.7
- 去掉了类型注解和 Python 3 特有语法
- 文件位置: 带有 `_py2` 后缀的文件

## 文件对照表

| Python 3 版本 | Python 2 兼容版本 | 说明 |
|--------------|------------------|------|
| `classic/quine.py` | `classic/quine_py2.py` | 基础 Quine |

## 验证 Quine

### Python 3
```bash
python3 classic/quine.py | diff - classic/quine.py
```

### Python 2
```bash
python classic/quine_py2.py | diff - classic/quine_py2.py
```

## 差异说明

Python 2 和 Python 3 版本的主要区别:

1. **print 语句/函数**
   - Python 2: `print s` (语句)
   - Python 3: `print(s)` (函数)

2. **字符串表示**
   - Python 2: `u'字符串'` 表示 Unicode
   - Python 3: 默认就是 Unicode

3. **编码声明**
   - 两者都支持 `# -*- coding: utf-8 -*-`

## 迁移指南

将 Python 3 Quine 转换为 Python 2:

```python
# Python 3
s='s=%r;print(s%%s)';print(s%s)

# Python 2  
s='s=%r;print s%%s';print s%s
```

## 测试环境

建议的测试环境:
- Python 3.8+ (主要开发目标)
- Python 2.7 (兼容性验证)
