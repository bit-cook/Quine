#!/usr/bin/env python3
#coding: utf-8
"""
衔尾蛇: Python 2 ↔ Python 3

这个程序在 Python 2 中运行输出 Python 3 版本
在 Python 3 中运行输出 Python 2 版本
两者循环往复

验证:
    python2 python2python3.py > p3.py
    python3 p3.py > p2.py
    diff python2python3.py p2.py  # 应该相同
"""

from __future__ import print_function

# Python 3 版本的代码
py3_version = '''#!/usr/bin/env python3
#coding: utf-8
"""
衔尾蛇: Python 2 ↔ Python 3

这个程序在 Python 2 中运行输出 Python 3 版本
在 Python 3 中运行输出 Python 2 版本
两者循环往复
"""

# Python 2 版本的代码
py2_version = """#!/usr/bin/env python3
#coding: utf-8
\\"""
衔尾蛇: Python 2 \\u2194 Python 3

这个程序在 Python 2 中运行输出 Python 3 版本
在 Python 3 中运行输出 Python 2 版本
两者循环往复
"""

from __future__ import print_function

# Python 3 版本的代码
py3_version = %r

print(py2_version)"""

print(py3_version)'''

print(py3_version)
