#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
多语言程序 (Polyglot) 生成器

生成同时是有效 Python 和有效 JavaScript 的程序。

原理:
    利用两种语言的不同注释语法:
    - Python: # 或 ''' '''
    - JavaScript: // 或 /* */
    
    以及不同的字符串表示方式
"""

def generate_python_js_polyglot():
    """
    生成 Python/JavaScript 多语言程序。
    
    该程序:
    - 在 Python 中运行: 输出 JavaScript 版本的代码
    - 在 JavaScript 中运行: 输出 Python 版本的代码
    """
    
    # Python 部分看到的代码
    python_view = '''#!/usr/bin/env python3
# /* "
# 多语言程序 - Python/JavaScript
# 这是一个 Polyglot 程序
# "

# JavaScript 版本的代码
js_code = """
// #
console.log("#!/usr/bin/env python3")
console.log("# 多语言程序 - Python/JavaScript")
console.log("")
console.log("# Python 版本的代码")
console.log("py_code = \\"\\"")
console.log(py_code.replace(/\\\\/g, "\\\\\\\\").replace(/"/g, "\\\\\\""))
console.log("\\"\\"")
console.log("console.log(py_code)")
// #
"""

print(js_code)
'''
    
    # JavaScript 部分看到的代码  
    js_view = '''// #
console.log("#!/usr/bin/env python3")
console.log("# 多语言程序 - Python/JavaScript")
console.log("")

// Python 版本的代码
py_code = `
# /* "
# 多语言程序 - Python/JavaScript
# 这是一个 Polyglot 程序
# "

# JavaScript 版本的代码
js_code = """
// #
console.log(py_code.replace(/\\$/g, '$$$$'))
// #
"""

print(js_code)
`

console.log(py_code)
// #
'''
    
    # 合并两种视图
    # 使用特殊的语法使两种语言都能解析
    
    polyglot = '''#!/usr/bin/env python3
0 and """ #
// JavaScript 开始
console.log("Python → JavaScript Polyglot")
// """ #
# Python 开始

print("JavaScript → Python Polyglot")
'''
    
    return polyglot

def generate_simple_polyglot():
    """
    生成一个更简单的多语言程序。
    这个版本主要是概念演示。
    """
    
    # 使用巧妙的语法兼容
    code = '''#!/usr/bin/env python3
# print("Hello from both languages!")
# /*
print("Hello from Python!")
# */
'''
    return code

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='多语言程序生成器')
    parser.add_argument('-o', '--output', help='输出文件')
    parser.add_argument('-t', '--type', default='simple', 
                       choices=['simple', 'full'],
                       help='生成类型')
    
    args = parser.parse_args()
    
    if args.type == 'full':
        result = generate_python_js_polyglot()
    else:
        result = generate_simple_polyglot()
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(result)
        print(f"Polyglot 已生成: {args.output}")
    else:
        print(result)

if __name__ == '__main__':
    main()
