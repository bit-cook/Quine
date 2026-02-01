#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Quine 验证器命令行工具 - Python 2 兼容版

验证一个程序是否为真正的 Quine。

使用方法:
    python quine_validator_py2.py <file> [options]
"""

import argparse
import sys
import subprocess
import difflib
import os


def validate_quine(filepath, command=None, encoding='utf-8', ignore_trailing_newline=False):
    """
    验证 Quine
    
    Args:
        filepath: 文件路径
        command: 运行命令
        encoding: 文件编码
        ignore_trailing_newline: 是否忽略结尾换行符
        
    Returns:
        是否通过验证
    """
    if not os.path.exists(filepath):
        print "错误: 文件不存在: %s" % filepath
        return False
    
    # 读取原始文件
    try:
        with open(filepath, 'r') as f:
            original = f.read()
    except Exception as e:
        print "错误: 无法读取文件: %s" % e
        return False
    
    # 确定运行命令
    if command is None:
        ext = os.path.splitext(filepath)[1].lower()
        if ext == '.py':
            command = ['python', filepath]
        elif ext == '.sh':
            command = ['bash', filepath]
        else:
            print "错误: 无法推断运行命令"
            return False
    
    print "验证文件: %s" % filepath
    print "运行命令: %s" % ' '.join(command)
    print "原始代码长度: %d 字符" % len(original)
    print "-" * 50
    
    # 运行程序
    try:
        proc = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = proc.communicate()
    except Exception as e:
        print "错误: 程序执行失败: %s" % e
        return False
    
    if proc.returncode != 0:
        print "错误: 程序执行失败 (返回码: %d)" % proc.returncode
        if stderr:
            print "错误输出:\n%s" % stderr
        return False
    
    output = stdout
    print "输出长度: %d 字符" % len(output)
    print "-" * 50
    
    # 比较
    compare_original = original
    compare_output = output
    
    if ignore_trailing_newline:
        compare_original = original.rstrip('\n')
        compare_output = output.rstrip('\n')
    
    if compare_original == compare_output:
        print "验证通过! 这是一个真正的 Quine。"
        return True
    else:
        print "验证失败!"
        
        if len(original) != len(output):
            print "长度不同: 原始=%d, 输出=%d" % (len(original), len(output))
        
        # 找出第一个差异
        min_len = min(len(compare_original), len(compare_output))
        for i in range(min_len):
            if compare_original[i] != compare_output[i]:
                print "\n第一个差异位置: %d" % i
                context = 20
                orig_ctx = repr(compare_original[max(0,i-context):i+context])
                out_ctx = repr(compare_output[max(0,i-context):i+context])
                print "原始: ...%s..." % orig_ctx
                print "输出: ...%s..." % out_ctx
                break
        
        return False


def main():
    parser = argparse.ArgumentParser(description='Quine 验证器')
    parser.add_argument('file', help='要验证的文件')
    parser.add_argument('--command', help='运行命令')
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
