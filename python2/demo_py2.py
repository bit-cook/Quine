#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Quine 项目演示脚本 - Python 2 兼容版

运行各种 Quine 示例并展示结果。
"""

import os
import sys
import subprocess


def print_header(title):
    print "\n" + "="*60
    print "  " + title
    print "="*60


def run_quine(filepath):
    """运行 Quine 并返回输出"""
    try:
        with open(filepath, 'r') as f:
            original = f.read()
        
        proc = subprocess.Popen(
            ['python', filepath],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = proc.communicate()
        output = stdout
        
        # 标准化换行符
        original = original.replace('\r\n', '\n').replace('\r', '\n')
        output = output.replace('\r\n', '\n').replace('\r', '\n')
        
        is_valid = (original == output)
        return original, output, is_valid
    except Exception as e:
        return "", str(e), False


def demo_basic_quine():
    print_header("演示 1: 基础 Python Quine")
    
    code = "s='s=%r;print(s%%s)';print(s%s)"
    print "\n  源代码:"
    print "  " + "-"*40
    print "  " + code
    print "  " + "-"*40
    
    print "\n  执行结果:"
    print "  " + "-"*40
    exec(code)
    print "  " + "-"*40
    print "\n  这是一个有效的 Quine!"


def demo_minimal_quine():
    print_header("演示 2: 极简 Quine (29字符)")
    
    code = "_='_=%r;print(_%%_)';print(_%_)"
    print "\n  源代码:"
    print "  " + "-"*40
    print "  " + code
    print "  " + "-"*40
    print "\n  代码长度: %d 字符" % len(code)
    
    print "\n  执行结果:"
    print "  " + "-"*40
    exec(code)
    print "  " + "-"*40


def demo_classic_quine():
    print_header("演示 3: 带注释的 Quine")
    
    filepath = "classic/quine_py2.py"
    if not os.path.exists(filepath):
        print "  文件不存在，跳过"
        return
    
    original, output, is_valid = run_quine(filepath)
    
    print "\n  代码长度: %d 字符" % len(original)
    print "  输出长度: %d 字符" % len(output)
    print "  验证结果: %s" % ("通过" if is_valid else "失败")


def demo_generator():
    print_header("演示 4: Quine 生成器")
    
    print "\n  生成一个自定义 Quine..."
    
    # 简单的生成示例
    custom_code = "print('Hello from generated Quine!')"
    template = "s=%r;exec(s);print(s)"
    generated = template % custom_code
    
    print "\n  自定义代码: %s" % custom_code
    print "\n  生成的 Quine:"
    print "  " + "-"*40
    print "  " + generated
    print "  " + "-"*40


def show_statistics():
    print_header("项目统计")
    
    counts = {
        "classic": 0,
        "variants": 0,
        "artistic": 0,
    }
    
    for category in counts.keys():
        if os.path.exists(category):
            files = [f for f in os.listdir(category) if f.endswith('.py')]
            counts[category] = len(files)
    
    total = sum(counts.values())
    
    print "\n  Quine 实现统计:"
    for cat, count in sorted(counts.items()):
        print "    %-12s: %d" % (cat, count)
    print "    %s: %s" % ("-"*12, "-"*3)
    print "    %-12s: %d" % ("总计", total)


def main():
    print """
    Quine - Self-Replicating Programs
    =================================
    
    自复制程序的艺术
    """
    
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    demo_basic_quine()
    demo_minimal_quine()
    demo_classic_quine()
    demo_generator()
    show_statistics()
    
    print_header("演示完成")
    print "\n  更多信息请查看:"
    print "    - README.md    项目介绍"
    print "    - EXAMPLES.md  更多示例"
    print


if __name__ == '__main__':
    main()
