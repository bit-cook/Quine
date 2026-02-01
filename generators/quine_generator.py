#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
通用 Quine 生成器

为任意 Python 代码生成 Quine 包装器。

使用方法:
    python quine_generator.py "print('Hello, World!')"
    
或者:
    python quine_generator.py -f my_script.py
"""

import argparse
import sys

def generate_quine(code: str) -> str:
    """
    为给定的 Python 代码生成 Quine。
    
    原理:
        使用 %r 格式化来正确转义所有特殊字符
    
    Args:
        code: 要包装成 Quine 的 Python 代码
        
    Returns:
        Quine 代码字符串
    """
    # 构建 Quine 模板
    template = '''#!/usr/bin/env python3
"""
自动生成的 Quine
原始代码:
%s
"""

# 数据部分
data = %r

# 代码部分
exec(data)

# Quine 验证代码
if '--verify' in __import__('sys').argv:
    import hashlib
    with open(__file__, 'r') as f:
        original = f.read()
    output = data
    if original == output:
        print("✓ Quine 验证通过!")
    else:
        print("✗ Quine 验证失败!")
        print(f"原始长度: {len(original)}")
        print(f"输出长度: {len(output)}")
'''
    
    # 格式化模板，嵌入原始代码
    quine = template % (code.replace('\\', '\\\\').replace('%', '%%'), code)
    
    return quine

def generate_minimal_quine(code: str = None) -> str:
    """
    生成极简 Quine（没有注释和验证代码）。
    
    Args:
        code: 可选的自定义代码，默认为简单的 print 语句
        
    Returns:
        极简 Quine 代码
    """
    if code is None:
        code = "print('Hello from Quine!')"
    
    # 极简模板
    template = "s=%r;exec(s);print(s)"
    quine = template % code
    
    return quine

def main():
    parser = argparse.ArgumentParser(
        description='Quine 生成器 - 将 Python 代码转换为自复制程序'
    )
    parser.add_argument(
        'code', 
        nargs='?',
        help='Python 代码字符串'
    )
    parser.add_argument(
        '-f', '--file',
        help='从文件读取代码'
    )
    parser.add_argument(
        '-m', '--minimal',
        action='store_true',
        help='生成极简版本（无注释）'
    )
    parser.add_argument(
        '-o', '--output',
        help='输出到文件'
    )
    
    args = parser.parse_args()
    
    # 获取代码
    if args.file:
        with open(args.file, 'r') as f:
            code = f.read()
    elif args.code:
        code = args.code
    else:
        # 默认代码
        code = '''#!/usr/bin/env python3
print("Hello, I am a generated Quine!")
print("Run me and I will output my own source code.")'''
    
    # 生成 Quine
    if args.minimal:
        quine = generate_minimal_quine(code)
    else:
        quine = generate_quine(code)
    
    # 输出
    if args.output:
        with open(args.output, 'w') as f:
            f.write(quine)
        print(f"Quine 已生成: {args.output}")
    else:
        print(quine)

if __name__ == '__main__':
    main()
