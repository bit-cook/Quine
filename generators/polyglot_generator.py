#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
多语言程序 (Polyglot) 生成器

生成同一个文件既能被 Python 3 解释、也能被 Node.js 执行的程序。

原理:
    * Python 把 `0//1` 当作整除(0)，随后 `\"\"\"...\"\"\"` 是一段多行字符串；
    * JavaScript 把 `0//1;\"\"\"` 行尾当作注释，从而跳过 Python 专属部分，
      并在 `process.exit(0)` 处停止，永不触达 Python 的 print。

生成的程序:
    * 以 python3 运行 -> 打印 "Hello from Python!"
    * 以 node   运行 -> 打印 "Hello from JavaScript!"

(若要“在两种语言里都输出自身源代码”的 Polyglot-Quine，属于高阶挑战，
 参见 CHALLENGES.md。)
"""


def generate_polyglot(message_py: str = "Hello from Python!",
                      message_js: str = "Hello from JavaScript!") -> str:
    return (
        "0//1;\"\"\"\n"
        "console.log(%r)\n"
        "process.exit(0)\n"
        "//\"\"\"\n"
        "print(%r)\n"
    ) % (message_js, message_py)


def generate_simple_polyglot() -> str:
    return generate_polyglot()


def main():
    import argparse

    parser = argparse.ArgumentParser(description="多语言程序 (Python/JavaScript) 生成器")
    parser.add_argument("-o", "--output", help="输出文件")
    parser.add_argument("--py", default="Hello from Python!", help="Python 侧消息")
    parser.add_argument("--js", default="Hello from JavaScript!", help="JavaScript 侧消息")

    args = parser.parse_args()
    result = generate_polyglot(args.py, args.js)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
        print("Polyglot 已生成: {}".format(args.output))
        print("验证: python3 {0}   &&   node {0}".format(args.output))
    else:
        print(result, end="")


if __name__ == "__main__":
    main()
