# Python 2 兼容版本

此目录包含 Python 2.7 兼容的 Quine 实现。

## 说明

**注意**: Python 2 已于 2020 年 1 月 1 日停止维护。这些文件仅用于兼容性目的。

推荐使用 Python 3 版本（见项目根目录的 `classic/`、`tests/`、`tools/` 等目录）。

## 文件列表

| 文件 | 说明 |
|------|------|
| `quine_py2.py` | 标准 Python 2 Quine |
| `quine_py2_compat.py` | Python 2/3 兼容版本 |
| `quine_generator_py2.py` | Quine 生成器 |
| `quine_validator_py2.py` | 验证工具 |
| `test_quine_py2.py` | 测试套件 |
| `utils_py2.py` | 测试工具 |
| `demo_py2.py` | 演示脚本 |
| `game_of_life_quine_py2.py` | 生命游戏 Quine |

## 使用方法

```bash
# 验证 Quine
python quine_py2.py | diff - quine_py2.py

# 运行测试
python test_quine_py2.py

# 运行演示
python demo_py2.py
```

## 差异说明

Python 2 和 Python 3 版本的主要区别：

1. **print 语句**: Python 2 使用 `print x`，Python 3 使用 `print(x)`
2. **字符串**: Python 2 区分 `str` 和 `unicode`
3. **类型注解**: Python 3 支持类型提示
4. **f-strings**: Python 3.6+ 支持格式化字符串字面值
