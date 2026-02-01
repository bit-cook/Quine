#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quine 验证器命令行工具

验证一个程序是否为真正的 Quine。

使用方法:
    python quine_validator.py <file> [options]

选项:
    --command CMD    自定义运行命令
    --encoding ENC   文件编码 (默认: utf-8)
    --ignore-trailing-newline  忽略结尾换行符差异
"""

import argparse
import sys
import subprocess
import difflib
from pathlib import Path


def validate_quine(filepath: str, 
                   command: list = None,
                   encoding: str = 'utf-8',
                   ignore_trailing_newline: bool = False) -> bool:
    """
    验证 Quine
    
    Args:
        filepath: 文件路径
        command: 运行命令 (默认: python <file>)
        encoding: 文件编码
        ignore_trailing_newline: 是否忽略结尾换行符
        
    Returns:
        是否通过验证
    """
    path = Path(filepath)
    
    if not path.exists():
        print(f"错误: 文件不存在: {filepath}")
        return False
    
    # 读取原始文件
    try:
        with open(path, 'r', encoding=encoding) as f:
            original = f.read()
    except Exception as e:
        print(f"错误: 无法读取文件: {e}")
        return False
    
    # 确定运行命令
    if command is None:
        # 根据文件扩展名推断
        ext = path.suffix.lower()
        if ext == '.py':
            command = ['python', str(path)]
        elif ext == '.js':
            command = ['node', str(path)]
        elif ext == '.sh':
            command = ['bash', str(path)]
        else:
            print(f"错误: 无法推断运行命令，请使用 --command 指定")
            return False
    
    print(f"验证文件: {filepath}")
    print(f"运行命令: {' '.join(command)}")
    print(f"原始代码长度: {len(original)} 字符")
    print("-" * 50)
    
    # 运行程序
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=30
        )
    except subprocess.TimeoutExpired:
        print("错误: 程序执行超时")
        return False
    except FileNotFoundError as e:
        print(f"错误: 找不到命令: {e}")
        return False
    
    if result.returncode != 0:
        print(f"错误: 程序执行失败 (返回码: {result.returncode})")
        if result.stderr:
            print(f"错误输出:\n{result.stderr}")
        return False
    
    output = result.stdout
    print(f"输出长度: {len(output)} 字符")
    print("-" * 50)
    
    # 比较
    compare_original = original
    compare_output = output
    
    if ignore_trailing_newline:
        compare_original = original.rstrip('\n')
        compare_output = output.rstrip('\n')
    
    if compare_original == compare_output:
        print("✓ 验证通过! 这是一个真正的 Quine。")
        return True
    else:
        print("✗ 验证失败!")
        
        # 显示差异
        if len(original) != len(output):
            print(f"长度不同: 原始={len(original)}, 输出={len(output)}")
        
        # 找出第一个差异
        min_len = min(len(compare_original), len(compare_output))
        for i in range(min_len):
            if compare_original[i] != compare_output[i]:
                print(f"\n第一个差异位置: {i}")
                context = 20
                orig_ctx = repr(compare_original[max(0,i-context):i+context])
                out_ctx = repr(compare_output[max(0,i-context):i+context])
                print(f"原始: ...{orig_ctx}...")
                print(f"输出: ...{out_ctx}...")
                break
        
        # 显示统一差异
        print("\n详细差异 (前 10 行):")
        diff = difflib.unified_diff(
            original.splitlines(keepends=True)[:20],
            output.splitlines(keepends=True)[:20],
            fromfile='original',
            tofile='output',
            lineterm=''
        )
        for line in list(diff)[:15]:
            print(line)
        
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Quine 验证器 - 验证程序是否为真正的 Quine'
    )
    parser.add_argument('file', help='要验证的文件')
    parser.add_argument('--command', help='运行命令 (如: "node file.js")')
    parser.add_argument('--encoding', default='utf-8', help='文件编码')
    parser.add_argument('--ignore-trailing-newline', action='store_true',
                       help='忽略结尾换行符的差异')
    
    args = parser.parse_args()
    
    command = args.command.split() if args.command else None
    
    success = validate_quine(
        args.file,
        command=command,
        encoding=args.encoding,
        ignore_trailing_newline=args.ignore_trailing_newline
    )
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
