#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quine 测试工具函数
"""

import subprocess
import tempfile
import os
from typing import Tuple, Optional


class QuineValidator:
    """Quine 验证器"""
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
    
    def log(self, message: str):
        """打印日志"""
        if self.verbose:
            print(f"[QuineValidator] {message}")
    
    def validate_python_quine(self, filepath: str) -> Tuple[bool, str]:
        """
        验证 Python Quine
        
        Args:
            filepath: Quine 文件路径
            
        Returns:
            (是否通过, 详细信息)
        """
        try:
            # 读取原始文件
            with open(filepath, 'r', encoding='utf-8') as f:
                original = f.read()
            
            self.log(f"读取文件: {filepath}")
            self.log(f"原始代码长度: {len(original)} 字符")
            
            # 运行程序获取输出
            result = subprocess.run(
                ['python', filepath],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode != 0:
                error_msg = f"程序执行失败:\n{result.stderr}"
                self.log(error_msg)
                return False, error_msg
            
            output = result.stdout
            self.log(f"输出长度: {len(output)} 字符")
            
            # 比较原始代码和输出
            if original == output:
                return True, f"✓ Quine 验证通过! ({len(original)} 字符)"
            else:
                # 找出差异
                diff_info = self._find_difference(original, output)
                return False, f"✗ Quine 验证失败\n{diff_info}"
                
        except subprocess.TimeoutExpired:
            return False, "✗ 程序执行超时"
        except FileNotFoundError:
            return False, f"✗ 文件未找到: {filepath}"
        except Exception as e:
            return False, f"✗ 验证过程出错: {str(e)}"
    
    def validate_quine_generic(self, 
                               filepath: str, 
                               command: list,
                               encoding: str = 'utf-8') -> Tuple[bool, str]:
        """
        通用 Quine 验证
        
        Args:
            filepath: 文件路径
            command: 执行命令列表 (如 ['node', 'quine.js'])
            encoding: 文件编码
            
        Returns:
            (是否通过, 详细信息)
        """
        try:
            with open(filepath, 'r', encoding=encoding) as f:
                original = f.read()
            
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode != 0:
                return False, f"程序执行失败:\n{result.stderr}"
            
            output = result.stdout
            
            if original == output:
                return True, f"✓ Quine 验证通过! ({len(original)} 字符)"
            else:
                diff_info = self._find_difference(original, output)
                return False, f"✗ Quine 验证失败\n{diff_info}"
                
        except Exception as e:
            return False, f"✗ 验证过程出错: {str(e)}"
    
    def _find_difference(self, original: str, output: str) -> str:
        """找出两个字符串的差异"""
        info = []
        
        if len(original) != len(output):
            info.append(f"长度不同: 原始={len(original)}, 输出={len(output)}")
        
        # 找出第一个不同的字符
        min_len = min(len(original), len(output))
        for i in range(min_len):
            if original[i] != output[i]:
                info.append(f"第一个差异位置: {i}")
                info.append(f"  原始: {repr(original[i:i+20])}")
                info.append(f"  输出: {repr(output[i:i+20])}")
                break
        
        # 检查结尾
        if original.rstrip() == output.rstrip():
            info.append("(注: 差异仅在结尾换行符)")
        
        return "\n".join(info)


def run_quine_test(filepath: str, language: str = 'python') -> bool:
    """
    简单的 Quine 测试函数
    
    Args:
        filepath: 文件路径
        language: 语言类型
        
    Returns:
        是否通过测试
    """
    validator = QuineValidator(verbose=True)
    
    commands = {
        'python': ['python', filepath],
        'javascript': ['node', filepath],
        'c': [filepath.replace('.c', '')],
        'rust': [filepath.replace('.rs', '')],
        'go': ['go', 'run', filepath],
        'java': ['java', filepath.replace('.java', '')],
    }
    
    if language in commands:
        success, msg = validator.validate_quine_generic(
            filepath, 
            commands[language]
        )
    else:
        success, msg = validator.validate_python_quine(filepath)
    
    print(msg)
    return success


if __name__ == '__main__':
    # 简单测试
    import sys
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        lang = sys.argv[2] if len(sys.argv) > 2 else 'python'
        run_quine_test(filepath, lang)
    else:
        print("用法: python utils.py <quine_file> [language]")
