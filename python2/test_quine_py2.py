#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Quine 项目测试套件 - Python 2 兼容版

运行所有 Quine 测试并生成报告。

使用方法:
    python test_quine_py2.py              # 运行所有测试
    python test_quine_py2.py -v           # 详细输出
    python test_quine_py2.py classic/     # 只测试指定目录
"""

import os
import sys
import argparse
from glob import glob

# 添加父目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils_py2 import QuineValidator


class QuineTestSuite:
    """Quine 测试套件"""
    
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.validator = QuineValidator(verbose=verbose)
        self.results = {}
    
    def log(self, message):
        """打印日志"""
        if self.verbose:
            print message
    
    def test_file(self, filepath):
        """
        测试单个 Quine 文件
        
        Args:
            filepath: 文件路径
            
        Returns:
            (是否通过, 消息)
        """
        ext = os.path.splitext(filepath)[1].lower()
        
        # 根据扩展名选择验证方法
        if ext == '.py':
            return self.validator.validate_python_quine(filepath)
        else:
            return False, "不支持的文件类型: %s" % ext
    
    def test_directory(self, directory):
        """
        测试目录中的所有 Quine 文件
        
        Args:
            directory: 目录路径
        """
        category = os.path.basename(directory)
        self.results[category] = []
        
        print "\n" + "="*60
        print "测试目录: %s" % directory
        print "="*60
        
        for filename in sorted(os.listdir(directory)):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath) and filename.endswith('.py'):
                print "\n测试: %s" % filename
                print "-" * 40
                success, msg = self.test_file(filepath)
                self.results[category].append((filename, success, msg))
                print msg
    
    def run_all_tests(self, base_dir):
        """运行所有测试"""
        print "="*60
        print "Quine 项目测试套件 (Python 2 兼容版)"
        print "="*60
        
        # 定义要测试的目录
        test_dirs = [
            os.path.join(base_dir, 'classic'),
            os.path.join(base_dir, 'variants'),
        ]
        
        for directory in test_dirs:
            if os.path.exists(directory):
                self.test_directory(directory)
    
    def generate_report(self):
        """生成测试报告"""
        report = []
        report.append("\n" + "="*60)
        report.append("测试报告")
        report.append("="*60)
        
        total_tests = 0
        total_passed = 0
        
        for category, results in self.results.items():
            report.append("\n【%s】" % category)
            for name, success, msg in results:
                status = "PASS" if success else "FAIL"
                report.append("  %s: %s" % (status, name))
                total_tests += 1
                if success:
                    total_passed += 1
        
        report.append("\n" + "-"*60)
        report.append("总计: %d/%d 通过" % (total_passed, total_tests))
        if total_tests > 0:
            percentage = (total_passed / float(total_tests)) * 100
            report.append("成功率: %.1f%%" % percentage)
        report.append("="*60)
        
        return "\n".join(report)
    
    def run(self, target=None):
        """
        运行测试套件
        
        Returns:
            退出码 (0 = 全部通过, 1 = 有失败)
        """
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        if target:
            if os.path.isfile(target):
                # 测试单个文件
                print "测试文件: %s" % target
                success, msg = self.test_file(target)
                print msg
                return 0 if success else 1
            elif os.path.isdir(target):
                # 测试目录
                self.test_directory(target)
            else:
                print "目标不存在: %s" % target
                return 1
        else:
            # 运行所有测试
            self.run_all_tests(base_dir)
        
        # 打印报告
        print self.generate_report()
        
        # 返回退出码
        for results in self.results.values():
            for _, success, _ in results:
                if not success:
                    return 1
        return 0


def main():
    parser = argparse.ArgumentParser(description='Quine 测试套件 (Python 2 兼容版)')
    parser.add_argument('target', nargs='?', help='指定测试的文件或目录')
    parser.add_argument('-v', '--verbose', action='store_true', help='详细输出')
    
    args = parser.parse_args()
    
    suite = QuineTestSuite(verbose=args.verbose)
    
    exit_code = suite.run(args.target)
    
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
