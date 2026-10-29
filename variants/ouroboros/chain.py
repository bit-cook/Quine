#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
多语言衔尾蛇链框架 (Ouroboros chain framework)

提供一个面向对象的 API，用来生成“自包含”的 N 节点闭环：第 i 个程序运行后
输出第 (i+1)%N 个程序的完整源代码，最后一个回到第一个。

核心技巧是“参数化旋转 Quine”：所有节点共享同一个自描述模板，仅用一个旋转
计数器 n 区分，因此无需在节点间互相嵌整份源码（那样会无限递归），也不读取
任何文件——每个节点自身都是一个严格的自复制不动点。

用法:
    from chain import OuroborosChain
    OuroborosChain(3).write(".")         # 写 3 个节点到当前目录
    python chain.py                       # 演示：打印 3 节点链的首个节点

说明:
    跨语言（如 Python→Ruby→C→Python）的衔尾蛇属于高阶挑战；本框架聚焦于
    单一语言内可严格验证的自包含闭环，详见 CHALLENGES.md。
"""


def node_source(index: int, count: int) -> str:
    s_val = (
        "# Ouroboros node (self-contained)\n"
        "n = %d\n"
        "N = %d\n"
        "s = %r\n"
        "print(s %% ((n + 1) %% N, N, s))"
    )
    return (
        "# Ouroboros node (self-contained)\n"
        "n = " + str(index) + "\n"
        "N = " + str(count) + "\n"
        "s = " + repr(s_val) + "\n"
        "print(s % ((n + 1) % N, N, s))\n"
    )


class OuroborosChain:
    """生成自包含的 N 节点衔尾蛇闭环。"""

    def __init__(self, count: int, prefix: str = "node_"):
        if count < 2:
            raise ValueError("count must be at least 2")
        self.count = count
        self.prefix = prefix

    def sources(self):
        return [node_source(i, self.count) for i in range(self.count)]

    def names(self):
        return ["{}{}.py".format(self.prefix, i) for i in range(self.count)]

    def write(self, directory: str):
        import os
        os.makedirs(directory, exist_ok=True)
        written = []
        for name, src in zip(self.names(), self.sources()):
            path = os.path.join(directory, name)
            with open(path, "w", encoding="utf-8") as f:
                f.write(src)
            written.append(path)
        return written


if __name__ == "__main__":
    chain = OuroborosChain(3, prefix="ouro_")
    print("# 3-node self-contained Ouroboros chain")
    print("# Node 0 source (run it to obtain node 1, and so on):\n")
    print(chain.sources()[0], end="")
    print("\n# Validate with:  python ../../tools/ouroboros_validator.py "
          "ouro_0.py ouro_1.py ouro_2.py")
