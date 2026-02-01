#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
二维码 Quine

生成一个二维码，扫描后得到源代码。

使用方法:
    python qr_quine.py              # 输出源代码（Quine 模式）
    python qr_quine.py --generate   # 生成二维码图片

需要安装 qrcode 库:
    pip install qrcode[pil]
"""

import sys

# 源代码字符串
# 注意: 这个字符串必须完全匹配文件内容
SOURCE_CODE = '''#!/usr/bin/env python3
"""
二维码 Quine

生成一个二维码，扫描后得到源代码。

使用方法:
    python qr_quine.py              # 输出源代码（Quine 模式）
    python qr_quine.py --generate   # 生成二维码图片

需要安装 qrcode 库:
    pip install qrcode[pil]
"""

import sys

# 源代码字符串
SOURCE_CODE = %r

def generate_qr(data, filename='quine_qr.png'):
    """生成二维码图片"""
    try:
        import qrcode
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        print(f"二维码已保存: {filename}")
        return True
    except ImportError:
        print("请先安装 qrcode 库: pip install qrcode[pil]")
        return False

def print_ascii_qr(data):
    """在终端打印 ASCII 二维码"""
    try:
        import qrcode
        qr = qrcode.QRCode(border=1)
        qr.add_data(data)
        qr.make()
        qr.print_ascii(invert=True)
        return True
    except ImportError:
        return False

if __name__ == '__main__':
    if '--generate' in sys.argv:
        # 生成二维码
        if not generate_qr(SOURCE_CODE):
            print("\\n尝试生成 ASCII 二维码:")
            print_ascii_qr(SOURCE_CODE)
    elif '--ascii' in sys.argv:
        print_ascii_qr(SOURCE_CODE)
    else:
        # Quine 模式: 输出源代码
        print(SOURCE_CODE %% SOURCE_CODE)
'''

def generate_qr(data, filename='quine_qr.png'):
    """生成二维码图片"""
    try:
        import qrcode
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        print(f"二维码已保存: {filename}")
        return True
    except ImportError:
        print("请先安装 qrcode 库: pip install qrcode[pil]")
        return False

def print_ascii_qr(data):
    """在终端打印 ASCII 二维码"""
    try:
        import qrcode
        qr = qrcode.QRCode(border=1)
        qr.add_data(data)
        qr.make()
        qr.print_ascii(invert=True)
        return True
    except ImportError:
        return False

if __name__ == '__main__':
    if '--generate' in sys.argv:
        # 生成二维码
        if not generate_qr(SOURCE_CODE):
            print("\n尝试生成 ASCII 二维码:")
            print_ascii_qr(SOURCE_CODE)
    elif '--ascii' in sys.argv:
        print_ascii_qr(SOURCE_CODE)
    else:
        # Quine 模式: 输出源代码
        print(SOURCE_CODE % SOURCE_CODE)
