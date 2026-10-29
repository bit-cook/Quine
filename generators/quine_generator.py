#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
通用 Quine 生成器 (Universal Quine Generator)

把任意 Python 代码包装成一个“真正的”自复制程序。

用法:
    python quine_generator.py "print('Hello, World!')"
    python quine_generator.py -f myscript.py -o my_quine.py
    python quine_generator.py --minimal

生成的程序:
    * 不带参数运行  -> 逐字节打印自身的源代码（真正的 Quine）
    * 带 --run 运行 -> 执行被包装的代码

生成原理:
    使用 %r 让 Python 自动完成所有转义，因此被包装的代码无需手动处理
    引号、反斜杠或百分号。整个文件由一个自描述模板重构而来。
"""

import argparse
import sys


def generate_quine(code: str) -> str:
    """为给定代码生成一个自复制程序（带 --run 时执行 code）。"""
    s_val = (
        "#!/usr/bin/env python3\n"
        "# -*- coding: utf-8 -*-\n"
        '"""\n'
        "自动生成的 Quine (Auto-generated Quine)\n"
        "不带参数运行会逐字节输出自身源代码；带 --run 运行则执行被包装的代码。\n"
        '"""\n'
        "import sys\n"
        "_s = %r\n"
        "_p = %r\n"
        "if '--run' in sys.argv:\n"
        "    exec(_p)\n"
        "else:\n"
        "    print(_s %% (_s, _p))"
    )
    return (
        "#!/usr/bin/env python3\n"
        "# -*- coding: utf-8 -*-\n"
        '"""\n'
        "自动生成的 Quine (Auto-generated Quine)\n"
        "不带参数运行会逐字节输出自身源代码；带 --run 运行则执行被包装的代码。\n"
        '"""\n'
        "import sys\n"
        "_s = " + repr(s_val) + "\n"
        "_p = " + repr(code) + "\n"
        "if '--run' in sys.argv:\n"
        "    exec(_p)\n"
        "else:\n"
        "    print(_s % (_s, _p))\n"
    )


def generate_minimal_quine() -> str:
    """经典的 29 字符极简 Quine。"""
    return "_='_=%r;print(_%%_)';print(_%_)"


def main():
    parser = argparse.ArgumentParser(description="Quine 生成器 - 将 Python 代码转换为自复制程序")
    parser.add_argument("code", nargs="?", help="要包装的 Python 代码字符串")
    parser.add_argument("-f", "--file", help="从文件读取代码")
    parser.add_argument("-m", "--minimal", action="store_true", help="生成经典极简 Quine")
    parser.add_argument("-o", "--output", help="输出到文件")

    args = parser.parse_args()

    if args.minimal:
        quine = generate_minimal_quine()
    else:
        if args.file:
            with open(args.file, "r", encoding="utf-8") as f:
                code = f.read()
        elif args.code:
            code = args.code
        else:
            code = 'print("Hello, I am a generated Quine!")'
        quine = generate_quine(code)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(quine)
        print("Quine 已生成: {}  (运行它验证: python {} | diff - {})".format(
            args.output, args.output, args.output))
    else:
        sys.stdout.write(quine)


if __name__ == "__main__":
    main()
