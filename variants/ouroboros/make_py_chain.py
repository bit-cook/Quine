#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自包含衔尾蛇链生成器 (Self-contained Ouroboros chain generator)

生成一个 N 节点的 Python 闭环：第 i 个程序运行后，输出第 (i+1)%N 个程序的
完整源代码，最后一个再回到第一个，形成“衔尾蛇”。

与“读取下一个文件”的朴素做法不同，这里每个节点都把整条链的共享模板内嵌在
自身源码中，通过一个旋转计数器 n 输出下一个节点——不依赖任何文件读写，
是严格的自复制结构（每个节点自身也是一个参数化 Quine 的不动点）。

用法:
    python make_py_chain.py 3
    # 生成 py_chain_0.py, py_chain_1.py, py_chain_2.py
    python ../../tools/ouroboros_validator.py   # 验证闭环性质
"""

import sys
import pathlib


def node_source(index: int, count: int) -> str:
    """Return the source of chain node `index` within a `count`-node cycle."""
    s_val = (
        "# 自包含衔尾蛇链节点 (self-contained Ouroboros node)\n"
        "n = %d\n"
        "N = %d\n"
        "s = %r\n"
        "print(s %% ((n + 1) %% N, N, s))"
    )
    return (
        "# 自包含衔尾蛇链节点 (self-contained Ouroboros node)\n"
        "n = " + str(index) + "\n"
        "N = " + str(count) + "\n"
        "s = " + repr(s_val) + "\n"
        "print(s % ((n + 1) % N, N, s))\n"
    )


def generate(count: int, prefix: str = "py_chain_") -> None:
    if count < 2:
        raise ValueError("count must be at least 2")
    base = pathlib.Path(__file__).parent
    for i in range(count):
        path = base / "{}{}.py".format(prefix, i)
        path.write_text(node_source(i, count), encoding="utf-8")
        print("Generated: {}".format(path.name))
    # Remove any stale higher-index files from a previous larger run.
    for stale in base.glob("{}*.py".format(prefix)):
        stem = stale.stem[len(prefix):]
        if stem.isdigit() and int(stem) >= count:
            stale.unlink()
            print("Removed stale: {}".format(stale.name))
    print("Successfully generated a self-contained chain of {} nodes in {}".format(count, base))


def main():
    if len(sys.argv) < 2:
        print("usage: python make_py_chain.py <count> [prefix]")
        sys.exit(1)
    count = int(sys.argv[1])
    prefix = sys.argv[2] if len(sys.argv) > 2 else "py_chain_"
    generate(count, prefix)


if __name__ == "__main__":
    main()
