#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
元 Quine 生成器 (Meta-Quine)

一个“生成 Quine 生成器”的程序。它输出一个可运行的 Quine 生成器源代码。

执行链:
    python meta_quine.py > my_generator.py
    python my_generator.py            # 打印一个有效的经典极简 Quine
    python my_generator.py | python3  # 运行该 Quine，验证其自复制

它本身不是 Quine，而是 Quine 生成器的“上游”。
"""

GENERATOR = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动生成的 Quine 生成器 (由 meta_quine.py 生成)

运行本文件会打印一个经典极简 Quine。
"""

# 经典 29 字符极简 Quine
QUINE = "_='_=%r;print(_%%_)';print(_%_)"


if __name__ == "__main__":
    print(QUINE)
'''


if __name__ == "__main__":
    print(GENERATOR, end="")
