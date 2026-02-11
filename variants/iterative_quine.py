#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
迭代 Quine (2-循环)

程序 A (本文件) 输出程序 B
程序 B 输出程序 A

使用方法:
    python iterative_quine.py > b.py
    python b.py | diff - iterative_quine.py
"""

# 程序 B 的代码
b_code = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
迭代 Quine (2-循环) - 程序 B

这是由程序 A 生成的程序 B
"""

# 程序 A 的代码
a_code = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\\"""
迭代 Quine (2-循环)

程序 A (本文件) 输出程序 B
程序 B 输出程序 A

使用方法:
    python iterative_quine.py > b.py
    python b.py | diff - iterative_quine.py
\\"""

# 程序 B 的代码
b_code = %r
print(a_code + (b_code %% b_code))"""

print(b_code % b_code)
'''

print(b_code % b_code)
