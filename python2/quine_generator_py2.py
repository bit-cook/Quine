#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
通用 Quine 生成器 - Python 2 兼容版

为任意 Python 代码生成 Quine 包装器。
"""

import argparse
import sys


def generate_quine(code):
    """
    为给定的 Python 代码生成 Quine。
    
    Args:
        code: 要包装成 Quine 的 Python 代码
        
    Returns:
        Quine 代码字符串
    """
    # 构建 Quine 模板
    template = '''#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
自动生成的 Quine
"""

# 数据部分
data = %r

# 代码部分
exec(data)

# 输出自身
print(data %% data)
'''
    
    # 格式化模板，嵌入原始代码
    quine = template % code
    
    return quine


def generate_minimal_quine(code=None):
    """
    生成极简 Quine（没有注释和验证代码）。
    
    Args:
        code: 可选的自定义代码
        
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
        code = "print('Hello, I am a generated Quine!')"
    
    # 生成 Quine
    if args.minimal:
        quine = generate_minimal_quine(code)
    else:
        quine = generate_quine(code)
    
    # 输出
    if args.output:
        with open(args.output, 'w') as f:
            f.write(quine)
        print "Quine 已生成: %s" % args.output
    else:
        print quine


if __name__ == '__main__':
    main()
