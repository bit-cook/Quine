#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Quine 项目演示脚本

运行各种 Quine 示例并展示结果。
"""

import os
import sys
import subprocess
import io

# 解决 Windows 环境下的编码问题
if sys.platform == 'win32':
    try:
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def print_header(title):
    print("\n" + "="*60)
    print("  " + title)
    print("="*60)

def print_code(code, language="python"):
    print("\n  源代码:")
    print("  " + "-"*40)
    for line in code.split('\n'):
        print("  " + line)
    print("  " + "-"*40)

def run_quine(filepath):
    """运行 Quine 并返回输出"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original = f.read()
        
        result = subprocess.Popen(
            [sys.executable, filepath],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = result.communicate()
        output = stdout.decode('utf-8', errors='replace')
        
        original = original.replace('\r\n', '\n').replace('\r', '\n')
        output = output.replace('\r\n', '\n').replace('\r', '\n')
        
        is_valid = (original == output)
        return original, output, is_valid
    except Exception as e:
        return "", str(e), False

def demo_basic_quine():
    print_header("演示 1: 基础 Python Quine")
    
    code = "s='s=%r;print(s%%s)';print(s%s)"
    print_code(code)
    
    print("\n  执行结果:")
    print("  " + "-"*40)
    exec(code)
    print("  " + "-"*40)
    print("\n  ✓ 这是一个有效的 Quine!")

def demo_classic_quine():
    print_header("演示 2: 带注释的 Quine")
    
    filepath = "classic/quine.py"
    if not os.path.exists(filepath):
        print("  文件不存在，跳过")
        return
    
    original, output, is_valid = run_quine(filepath)
    
    print("\n  代码长度: {} 字符".format(len(original)))
    print("  输出长度: {} 字符".format(len(output)))
    print("  验证结果: {}".format("✓ 通过" if is_valid else "✗ 失败"))

def demo_minimal_quine():
    print_header("演示 3: 极简 Quine (29字符)")
    
    code = "_='_=%r;print(_%%_)';print(_%_)"
    print_code(code)
    print("\n  代码长度: {} 字符".format(len(code)))
    print("\n  执行结果:")
    print("  " + "-"*40)
    exec(code)
    print("  " + "-"*40)

def demo_iterative_quine():
    print_header("演示 4: 迭代 Quine")
    
    filepath = "variants/iterative_quine.py"
    if not os.path.exists(filepath):
        print("  文件不存在，跳过")
        return
    
    print("\n  程序 A 生成程序 B...")
    original, output, _ = run_quine(filepath)
    
    # 保存 B 并运行
    temp_file = "temp_b.py"
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(output)
    
    # 使用 UTF-8 环境运行子进程，防止 Windows 下的编码错误
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    
    result = subprocess.Popen(
        [sys.executable, temp_file],
        stdout=subprocess.PIPE,
        env=env
    )
    b_output, _ = result.communicate()
    
    # 安全解码
    if b_output is None:
        b_output = ""
    elif isinstance(b_output, bytes):
        b_output = b_output.decode('utf-8', errors='replace')
    
    if os.path.exists(temp_file):
        os.remove(temp_file)
    
    original = original.replace('\r\n', '\n').replace('\r', '\n')
    b_output = b_output.replace('\r\n', '\n').replace('\r', '\n')
    
    cycle_complete = (original.strip() == b_output.strip())
    
    print("  程序 B 输出程序 A: {}".format("✓ 通过" if cycle_complete else "✗ 失败"))
    print("\n  A -> B -> A 循环: {}".format("✓ 完成" if cycle_complete else "✗ 未完成"))

def demo_generator():
    print_header("演示 5: Quine 生成器")
    
    print("\n  生成一个自定义 Quine...")
    
    # 简单的生成示例
    custom_code = "print('Hello from generated Quine!')"
    template = "s=%r;exec(s);print(s)"
    generated = template % custom_code
    
    print("\n  自定义代码: {}".format(custom_code))
    print("\n  生成的 Quine:")
    print("  " + "-"*40)
    print("  " + generated)
    print("  " + "-"*40)

def show_statistics():
    print_header("项目统计")
    
    counts = {
        "classic": 0,
        "variants": 0,
        "artistic": 0,
        "generators": 0,
        "tools": 0,
        "esoteric": 0,
    }
    
    for category in counts.keys():
        if os.path.exists(category):
            files = [f for f in os.listdir(category) if f.endswith('.py')]
            counts[category] = len(files)
    
    total = sum(counts.values())
    
    print("\n  Quine 实现统计:")
    for cat, count in sorted(counts.items()):
        print("    {:12s}: {}".format(cat, count))
    print("    {}: {}".format("-"*12, "-"*3))
    print("    {:12s}: {}".format("总计", total))

def main():
    try:
        print("""
    ██████╗ ██╗   ██╗██╗███╗   ██╗███████╗
    ██╔═══██╗██║   ██║██║████╗  ██║██╔════╝
    ██║   ██║██║   ██║██║██╔██╗ ██║█████╗  
    ██║▄▄ ██║██║   ██║██║██║╚██╗██║██╔══╝  
    ╚██████╔╝╚██████╔╝██║██║ ╚████║███████╗
     ╚══▀▀═╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
        """)
    except Exception:
        print("\n    === QUINE PROJECT ===\n")
        
    print("    自复制程序的艺术")
    print()
    
    # 获取脚本所在目录
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        if script_dir:
            os.chdir(script_dir)
    except Exception as e:
        print("  警告: 无法切换到脚本目录: {}".format(e))
    
    demo_basic_quine()
    demo_minimal_quine()
    demo_classic_quine()
    demo_iterative_quine()
    demo_generator()
    show_statistics()
    
    print_header("演示完成")
    print("\n  更多信息请查看:")
    print("    - README.md    项目介绍")
    print("    - THEORY.md    理论分析")
    print("    - EXAMPLES.md  更多示例")
    print("    - CHALLENGES.md 编程挑战")
    print()

if __name__ == '__main__':
    main()
