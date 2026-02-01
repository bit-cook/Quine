#!/usr/bin/env python3
#coding: utf-8
"""
多语言 Quine - Python 2 和 Python 3 兼容

这个文件既是有效的 Python 2 程序，也是有效的 Python 3 程序。
在两种语言中运行都会输出相同的源代码。

验证:
    python2 multiquine.py | diff - multiquine.py
    python3 multiquine.py | diff - multiquine.py
"""

from __future__ import print_function

s = '#!/usr/bin/env python3\n#coding: utf-8\n"""\n多语言 Quine - Python 2 和 Python 3 兼容\n\n这个文件既是有效的 Python 2 程序，也是有效的 Python 3 程序。\n在两种语言中运行都会输出相同的源代码。\n\n验证:\n    python2 multiquine.py | diff - multiquine.py\n    python3 multiquine.py | diff - multiquine.py\n"""\n\nfrom __future__ import print_function\n\ns = %r\nprint(s %% s)'
print(s % s)
