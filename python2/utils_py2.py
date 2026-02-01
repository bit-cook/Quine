#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Quine 测试工具函数 - Python 2 兼容版
"""

import subprocess
import tempfile
import os


class QuineValidator:
    """Quine 验证器"""
    
    def __init__(self, verbose=False):
        self.verbose = verbose
    
    def log(self, message):
        """打印日志"""
        if self.verbose:
            print "[QuineValidator] %s" % message
    
    def validate_python_quine(self, filepath):
        """
        验证 Python Quine
        
        Args:
            filepath: Quine 文件路径
            
        Returns:
            (是否通过, 详细信息)
        """
        try:
            # 读取原始文件
            with open(filepath, 'r') as f:
                original = f.read()
            
            self.log("读取文件: %s" % filepath)
            self.log("原始代码长度: %d 字符" % len(original))
            
            # 运行程序获取输出
            proc = subprocess.Popen(
                ['python', filepath],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = proc.communicate()
            
            if proc.returncode != 0:
                error_msg = "程序执行失败:\n%s" % stderr
                self.log(error_msg)
                return False, error_msg
            
            output = stdout
            self.log("输出长度: %d 字符" % len(output))
            
            # 比较原始代码和输出
            if original == output:
                return True, "Quine 验证通过! (%d 字符)" % len(original)
            else:
                # 找出差异
                diff_info = self._find_difference(original, output)
                return False, "Quine 验证失败\n%s" % diff_info
                
        except subprocess.TimeoutExpired:
            return False, "程序执行超时"
        except Exception as e:
            return False, "验证过程出错: %s" % str(e)
    
    def _find_difference(self, original, output):
        """找出两个字符串的差异"""
        info = []
        
        if len(original) != len(output):
            info.append("长度不同: 原始=%d, 输出=%d" % (len(original), len(output)))
        
        # 找出第一个不同的字符
        min_len = min(len(original), len(output))
        for i in range(min_len):
            if original[i] != output[i]:
                info.append("第一个差异位置: %d" % i)
                orig_ctx = repr(original[max(0,i-20):i+20])
                out_ctx = repr(output[max(0,i-20):i+20])
                info.append("  原始: ...%s..." % orig_ctx)
                info.append("  输出: ...%s..." % out_ctx)
                break
        
        # 检查结尾
        if original.rstrip() == output.rstrip():
            info.append("(注: 差异仅在结尾换行符)")
        
        return "\n".join(info)


def run_quine_test(filepath, language='python'):
    """
    简单的 Quine 测试函数
    
    Args:
        filepath: 文件路径
        language: 语言类型
        
    Returns:
        是否通过测试
    """
    validator = QuineValidator(verbose=True)
    
    if language == 'python':
        success, msg = validator.validate_python_quine(filepath)
    else:
        success, msg = False, "不支持的类型"
    
    print msg
    return success


if __name__ == '__main__':
    # 简单测试
    import sys
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        lang = sys.argv[2] if len(sys.argv) > 2 else 'python'
        run_quine_test(filepath, lang)
    else:
        print "用法: python utils_py2.py <quine_file> [language]"
