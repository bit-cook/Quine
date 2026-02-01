#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quine 可视化工具

可视化 Quine 的自我复制过程。
"""

import argparse
import sys
import time


def visualize_quine_execution(code: str, delay: float = 0.5):
    """
    可视化 Quine 的执行过程
    
    Args:
        code: Quine 源代码
        delay: 每步之间的延迟（秒）
    """
    print("=" * 60)
    print("Quine 执行过程可视化")
    print("=" * 60)
    
    # 步骤 1: 显示源代码
    print("\n【步骤 1】源代码:")
    print("-" * 60)
    print(code)
    print("-" * 60)
    time.sleep(delay)
    
    # 步骤 2: 提取数据部分
    print("\n【步骤 2】数据部分 (字符串变量):")
    print("-" * 60)
    
    # 简单的数据提取（假设使用 s = '...' 格式）
    if "s = " in code or "s=" in code:
        lines = code.split('\n')
        for line in lines:
            if 's=' in line or 's =' in line:
                print(f"找到数据: {line[:50]}...")
                break
    print("-" * 60)
    time.sleep(delay)
    
    # 步骤 3: 执行输出
    print("\n【步骤 3】执行 print(s % s):")
    print("-" * 60)
    
    try:
        # 执行代码并捕获输出
        import io
        import contextlib
        
        output_buffer = io.StringIO()
        with contextlib.redirect_stdout(output_buffer):
            exec(code)
        
        output = output_buffer.getvalue()
        print(f"输出长度: {len(output)} 字符")
        print(f"输出预览: {output[:100]}...")
        
    except Exception as e:
        print(f"执行出错: {e}")
    
    print("-" * 60)
    time.sleep(delay)
    
    # 步骤 4: 验证
    print("\n【步骤 4】验证:")
    print("-" * 60)
    
    try:
        if output.strip() == code.strip():
            print("✓ 输出与源代码完全匹配!")
            print("✓ 这是一个真正的 Quine!")
        else:
            print("✗ 输出与源代码不匹配")
            print(f"  原始: {len(code)} 字符")
            print(f"  输出: {len(output)} 字符")
    except:
        pass
    
    print("-" * 60)


def visualize_quine_structure():
    """可视化 Quine 的结构"""
    
    print("=" * 60)
    print("Quine 结构图")
    print("=" * 60)
    
    print("""
    ┌─────────────────────────────────────────────────────────┐
    │                      Quine 结构                         │
    ├─────────────────────────────────────────────────────────┤
    │                                                         │
    │   ┌──────────────┐         ┌──────────────┐            │
    │   │   数据部分    │◄───────►│   代码部分    │            │
    │   │  (源代码的    │         │  (输出逻辑)   │            │
    │   │   字符串)     │         │              │            │
    │   └──────┬───────┘         └──────┬───────┘            │
    │          │                        │                    │
    │          │    ┌──────────┐        │                    │
    │          └───►│  print() │◄───────┘                    │
    │               └────┬─────┘                             │
    │                    │                                    │
    │                    ▼                                    │
    │              ┌──────────┐                               │
    │              │  输出    │                               │
    │              │ 源代码   │                               │
    │              └──────────┘                               │
    │                                                         │
    └─────────────────────────────────────────────────────────┘
    
    经典 Quine 公式:
    ┌────────────────────────────────────────────────────────┐
    │  s = 's = %r\\nprint(s %% s)'                           │
    │  print(s % s)                                          │
    │                                                        │
    │  变量 s 存储代码本身                                   │
    │  print(s % s) 输出 s 并将 s 本身填入 %r 位置          │
    └────────────────────────────────────────────────────────┘
    """)


def animate_quine_generation():
    """动画演示 Quine 的生成过程"""
    
    print("=" * 60)
    print("Quine 生成动画")
    print("=" * 60)
    
    # 开始状态
    template = "s = '...'; print(s % s)"
    
    print("\n从模板开始:")
    print(f"  {template}")
    time.sleep(1)
    
    # 填充数据
    data = "print('Hello')"
    print(f"\n1. 定义数据部分: {data}")
    time.sleep(0.5)
    
    # 构造 Quine
    step2 = f"s = '{data}'; print(s % s)"
    print(f"\n2. 将数据放入模板:")
    print(f"   {step2}")
    time.sleep(0.5)
    
    # 处理转义
    print(f"\n3. 但这样不对！我们需要 s 包含整个代码...")
    time.sleep(0.5)
    
    # 正确的 Quine
    quine = "s='s=%r;print(s%%s)';print(s%s)"
    print(f"\n4. 正确的自引用结构:")
    print(f"   {quine}")
    time.sleep(0.5)
    
    print(f"\n5. 执行时:")
    print(f"   s % s 将 s 本身填入 %r 位置")
    print(f"   输出与源代码完全相同！")


def main():
    parser = argparse.ArgumentParser(description='Quine 可视化工具')
    parser.add_argument('file', nargs='?', help='要可视化的 Quine 文件')
    parser.add_argument('--structure', action='store_true', help='显示结构图')
    parser.add_argument('--animate', action='store_true', help='动画演示')
    parser.add_argument('--delay', type=float, default=0.5, help='动画延迟')
    
    args = parser.parse_args()
    
    if args.structure:
        visualize_quine_structure()
    elif args.animate:
        animate_quine_generation()
    elif args.file:
        try:
            with open(args.file, 'r') as f:
                code = f.read()
            visualize_quine_execution(code, args.delay)
        except FileNotFoundError:
            print(f"文件未找到: {args.file}")
            sys.exit(1)
    else:
        # 默认显示结构
        visualize_quine_structure()


if __name__ == '__main__':
    main()
