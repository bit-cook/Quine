#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quine 项目测试套件

运行所有 Quine 测试并生成报告。

使用方法:
    python test_quine.py              # 运行所有测试
    python test_quine.py -v           # 详细输出
    python test_quine.py classic/     # 只测试指定目录
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Tuple

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent))
from utils import QuineValidator


class QuineTestSuite:
    """Quine 测试套件"""
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.validator = QuineValidator(verbose=verbose)
        self.results: Dict[str, List[Tuple[str, bool, str]]] = {}
    
    def log(self, message: str):
        """打印日志"""
        if self.verbose:
            print(message)
    
    def test_file(self, filepath: Path) -> Tuple[bool, str]:
        """
        测试单个 Quine 文件
        
        Args:
            filepath: 文件路径
            
        Returns:
            (是否通过, 消息)
        """
        ext = filepath.suffix.lower()
        
        # 根据扩展名选择验证方法
        if ext == '.py':
            return self.validator.validate_python_quine(str(filepath))
        elif ext == '.js':
            return self.validator.validate_quine_generic(
                str(filepath), ['node', str(filepath)]
            )
        elif ext == '.c':
            # 需要编译
            exe_path = str(filepath.with_suffix(''))
            compile_result = os.system(f'gcc -o "{exe_path}" "{filepath}" 2>/dev/null')
            if compile_result != 0:
                return False, "编译失败"
            return self.validator.validate_quine_generic(
                str(filepath), [exe_path]
            )
        elif ext == '.rs':
            return self.validator.validate_quine_generic(
                str(filepath), ['rustc', '-o', str(filepath.with_suffix('')), str(filepath)]
            )
        elif ext == '.go':
            return self.validator.validate_quine_generic(
                str(filepath), ['go', 'run', str(filepath)]
            )
        elif ext == '.java':
            # 需要编译
            compile_result = os.system(f'javac "{filepath}" 2>/dev/null')
            if compile_result != 0:
                return False, "编译失败"
            class_name = filepath.stem
            return self.validator.validate_quine_generic(
                str(filepath), ['java', '-cp', str(filepath.parent), class_name]
            )
        elif ext == '.sh':
            return self.validator.validate_quine_generic(
                str(filepath), ['bash', str(filepath)]
            )
        else:
            return False, f"不支持的文件类型: {ext}"
    
    def test_directory(self, directory: Path) -> None:
        """
        测试目录中的所有 Quine 文件
        
        Args:
            directory: 目录路径
        """
        category = directory.name
        self.results[category] = []
        
        print(f"\n{'='*60}")
        print(f"测试目录: {directory}")
        print('='*60)
        
        for filepath in directory.iterdir():
            if filepath.is_file() and filepath.suffix in ['.py', '.js', '.c', '.rs', '.go', '.java', '.sh']:
                print(f"\n测试: {filepath.name}")
                print('-' * 40)
                success, msg = self.test_file(filepath)
                self.results[category].append((filepath.name, success, msg))
                print(msg)
    
    def run_all_tests(self, base_dir: Path) -> None:
        """运行所有测试"""
        print("="*60)
        print("Quine 项目测试套件")
        print("="*60)
        
        # 定义要测试的目录
        test_dirs = [
            base_dir / 'classic',
            base_dir / 'variants',
            base_dir / 'artistic',
        ]
        
        for directory in test_dirs:
            if directory.exists():
                self.test_directory(directory)
    
    def generate_report(self) -> str:
        """生成测试报告"""
        report = []
        report.append("\n" + "="*60)
        report.append("测试报告")
        report.append("="*60)
        
        total_tests = 0
        total_passed = 0
        
        for category, results in self.results.items():
            report.append(f"\n【{category}】")
            for name, success, msg in results:
                status = "✓ PASS" if success else "✗ FAIL"
                report.append(f"  {status}: {name}")
                total_tests += 1
                if success:
                    total_passed += 1
        
        report.append("\n" + "-"*60)
        report.append(f"总计: {total_passed}/{total_tests} 通过")
        if total_tests > 0:
            percentage = (total_passed / total_tests) * 100
            report.append(f"成功率: {percentage:.1f}%")
        report.append("="*60)
        
        return "\n".join(report)
    
    def run(self, target: Path = None) -> int:
        """
        运行测试套件
        
        Returns:
            退出码 (0 = 全部通过, 1 = 有失败)
        """
        base_dir = Path(__file__).parent.parent
        
        if target:
            if target.is_file():
                # 测试单个文件
                print(f"测试文件: {target}")
                success, msg = self.test_file(target)
                print(msg)
                return 0 if success else 1
            elif target.is_dir():
                # 测试目录
                self.test_directory(target)
            else:
                print(f"目标不存在: {target}")
                return 1
        else:
            # 运行所有测试
            self.run_all_tests(base_dir)
        
        # 打印报告
        print(self.generate_report())
        
        # 返回退出码
        for results in self.results.values():
            for _, success, _ in results:
                if not success:
                    return 1
        return 0


def main():
    parser = argparse.ArgumentParser(description='Quine 测试套件')
    parser.add_argument('target', nargs='?', help='指定测试的文件或目录')
    parser.add_argument('-v', '--verbose', action='store_true', help='详细输出')
    
    args = parser.parse_args()
    
    suite = QuineTestSuite(verbose=args.verbose)
    
    target = Path(args.target) if args.target else None
    exit_code = suite.run(target)
    
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
