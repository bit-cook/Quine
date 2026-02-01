#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quine 大小优化器

分析和优化 Quine 的代码大小。

使用方法:
    python size_optimizer.py <file>
"""

import argparse
import re
from pathlib import Path


def analyze_quine(filepath: str):
    """分析 Quine 的代码结构"""
    
    with open(filepath, 'r') as f:
        code = f.read()
    
    lines = code.split('\n')
    
    print(f"文件: {filepath}")
    print("=" * 50)
    print(f"总字符数: {len(code)}")
    print(f"总行数: {len(lines)}")
    print(f"非空行数: {sum(1 for l in lines if l.strip())}")
    print(f"空格数: {code.count(' ')}")
    print(f"换行数: {code.count(chr(10))}")
    print()
    
    # 分析代码结构
    print("代码结构分析:")
    print("-" * 50)
    
    # 查找字符串赋值
    string_pattern = r"([a-zA-Z_]\w*)\s*=\s*['\"]"
    matches = re.findall(string_pattern, code)
    if matches:
        print(f"字符串变量: {', '.join(set(matches))}")
    
    # 查找 print 语句
    print_count = len(re.findall(r'\bprint\s*\(', code))
    print(f"print 调用: {print_count}")
    
    # 查找格式化操作
    format_ops = len(re.findall(r'%[srdf]', code))
    print(f"格式化操作: {format_ops}")
    
    # 优化建议
    print()
    print("优化建议:")
    print("-" * 50)
    
    suggestions = []
    
    if code.count('    ') > 10:
        suggestions.append("使用空格而非 Tab/4空格可以节省字符")
    
    if '\n\n' in code:
        suggestions.append("删除空行可以节省字符")
    
    if '    ' in code:
        suggestions.append("减少缩进可以节省字符")
    
    # 检查是否使用了 %r
    if '%r' in code:
        suggestions.append("✓ 已使用 %r 进行自动转义（推荐）")
    
    # 检查是否有注释
    comment_lines = [l for l in lines if l.strip().startswith('#')]
    if len(comment_lines) > 1:  # 允许 shebang
        suggestions.append(f"删除 {len(comment_lines)-1} 行注释可以节省字符")
    
    # 检查 docstring
    if '"""' in code or "'''" in code:
        suggestions.append("删除 docstring 可以显著减少字符数")
    
    if not suggestions:
        print("代码已经很精简了！")
    else:
        for i, s in enumerate(suggestions, 1):
            print(f"{i}. {s}")


def generate_minimal_template():
    """生成极简 Quine 模板"""
    
    templates = {
        'python': "_='_=%r;print(_%%_)';print(_%_)",
        'javascript': "(a=>console.log('('+a+')('+JSON.stringify(a)+')'))('a=>console.log('+'('+a+')('+JSON.stringify(a)+')')')",
        'ruby': 's=%q{s=%q{s};printf s,s};printf s,s',
        'perl': '$s=\'$s=%s;printf $s,\'"\'"\'$s\'"\'"\';\'"\'"\';printf $s,\'"\'"\'$s\'"\'"\'',
    }
    
    print("\n极简 Quine 模板:")
    print("=" * 50)
    
    for lang, template in templates.items():
        print(f"\n{lang} ({len(template)} 字符):")
        print(f"  {template}")


def main():
    parser = argparse.ArgumentParser(description='Quine 大小优化器')
    parser.add_argument('file', nargs='?', help='要分析的文件')
    parser.add_argument('--templates', action='store_true', help='显示极简模板')
    
    args = parser.parse_args()
    
    if args.templates:
        generate_minimal_template()
    elif args.file:
        analyze_quine(args.file)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
