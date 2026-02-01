#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
元 Quine 生成器 (Meta-Quine)

一个生成 Quine 生成器的程序。这不是 Quine 本身，
但输出一个程序，后者输出一个 Quine。

执行链:
    meta_quine.py → quine_generator.py → quine.py
"""

def main():
    """
    输出一个 Quine 生成器。
    """
    
    # 这是将要输出的 Quine 生成器的代码
    generator_code = '''#!/usr/bin/env python3
"""
自动生成的 Quine 生成器

由 meta_quine.py 生成
"""

def generate_quine():
    """
    生成一个标准的 Quine。
    """
    # Quine 的核心代码
    s = 's = %r\\nprint(s %% s)'
    return s %% s

if __name__ == '__main__':
    print(generate_quine())
'''
    
    print(generator_code)

if __name__ == '__main__':
    main()
