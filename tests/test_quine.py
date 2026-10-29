#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quine 测试套件入口（兼容旧接口）。

本文件现在委托给主验证器 tools/validate_all.py——它是唯一的事实来源，
能针对每种 Quine 的类型（self / cycle / chain / emitter / multiling / generator）
采用正确判据。

用法:
    python tests/test_quine.py            # 验证全部
    python tests/test_quine.py -v         # 详细输出
    python tests/test_quine.py classic    # 只验证某目录/文件
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))

import validate_all  # noqa: E402

if __name__ == "__main__":
    sys.argv = ["validate_all"] + sys.argv[1:]
    validate_all.main()
