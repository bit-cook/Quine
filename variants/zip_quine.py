#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZIP Quine — 概念演示 (conceptual demonstration)

目标：产出一个 ZIP 文件，使得 `unzip -p quine.zip` 得到的文件内容
恰好等于该 ZIP 文件本身（即 ZIP 里“装着”自己）。

    python zip_quine.py > quine.zip
    unzip -p quine.zip | cmp - quine.zip      # 若一致即为 ZIP Quine

现状与难点：
    本脚本演示 ZIP 结构（本地文件头 / 中央目录 / 结束记录），并给出一个
    “自指”的构造思路，但**尚未**达成字节级自包含。真正的 ZIP Quine 需要解
    一个关于 DEFLATE 压缩流的不动点方程：

        Z = LFH + raw_deflate(Z) + CD + EOCD

    由于 DEFLATE 对自身输出的压缩并不收敛（会振荡），必须精心构造压缩流
    （例如混用存储块）才能得到不动点——这属于高阶挑战，见 CHALLENGES.md。

因此本文件定位为“教学用 ZIP 构造器 + 概念说明”，而非一个已臻完善的 Quine。
"""

import io
import struct
import sys
import zipfile
import zlib


def build_demo_zip() -> bytes:
    """构造一个结构完整、可被标准工具读取的 ZIP（含内嵌的说明文本）。"""
    buf = io.BytesIO()
    note = (
        b"This ZIP demonstrates the local-header / central-directory / EOCD "
        b"layout used when building a self-containing (Quine) ZIP. A true ZIP "
        b"Quine must additionally solve a DEFLATE fixed-point; see docstring."
    )
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("README.txt", note)
    return buf.getvalue()


def describe_layout(data: bytes) -> str:
    lines = ["ZIP 结构解析:"]
    eocd_sig = 0x06054B50
    idx = data.rfind(struct.pack("<I", eocd_sig))
    if idx != -1:
        (_, _, _, _, total, cd_size, cd_off, _) = struct.unpack("<IHHHHIIH", data[idx:idx + 22])
        lines.append(f"  EOCD @ {idx}: entries={total}, central-dir @ {cd_off} (size {cd_size})")
    lines.append(f"  总大小: {len(data)} 字节")
    return "\n".join(lines)


if __name__ == "__main__":
    data = build_demo_zip()
    sys.stdout.buffer.write(data)
    # 说明信息写到 stderr，避免污染 stdout 的 ZIP 字节流
    print(describe_layout(data), file=sys.stderr)
