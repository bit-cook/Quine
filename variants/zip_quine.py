#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZIP Quine 生成器

生成一个 ZIP 文件，解压后包含的文件内容就是 ZIP 文件本身。

使用方法:
    python zip_quine.py > quine.zip
    unzip -p quine.zip | diff - quine.zip

注意: 这是一个生成器，不是 Quine 本身
"""

import struct
import zlib
import io

def create_zip_quine():
    """
    创建一个 ZIP 文件，其内容是自身的副本。
    
    ZIP 文件格式:
    [本地文件头1][文件数据1][数据描述符1]...
    [中央目录][中央目录结束记录]
    """
    
    # 文件名
    filename = "quine.zip"
    
    # 我们需要的文件内容（循环引用）
    # 这是一个简化版本，真正的 ZIP Quine 需要精确构造
    
    output = io.BytesIO()
    
    # 写入本地文件头
    local_header = struct.pack('<IHHHHHIIIHH',
        0x04034b50,  # 本地文件头签名
        20,          # 版本
        0,           # 标志
        8,           # 压缩方法 (deflate)
        0,           # 修改时间
        0,           # 修改日期
        0,           # CRC-32 (占位)
        0,           # 压缩大小 (占位)
        0,           # 未压缩大小 (占位)
        len(filename),
        0            # 额外字段长度
    )
    
    output.write(local_header)
    output.write(filename.encode())
    
    # 文件数据（这里需要是自身的引用，这是难点）
    # 真正的实现需要精确计算偏移量
    file_data = b"This would be the self-referential content"
    compressed = zlib.compress(file_data)
    output.write(compressed)
    
    # 中央目录
    central_header = struct.pack('<IHHHHHHIIIHHHHHII',
        0x02014b50,  # 中央目录签名
        20,          # 创建版本
        20,          # 需要版本
        0,           # 标志
        8,           # 压缩方法
        0, 0,        # 时间/日期
        0,           # CRC-32
        len(compressed),
        len(file_data),
        len(filename),
        0, 0, 0,     # 额外字段、注释、磁盘
        0,           # 内部属性
        0,           # 外部属性
        0            # 本地头部偏移
    )
    
    output.write(central_header)
    output.write(filename.encode())
    
    # 中央目录结束记录
    end_record = struct.pack('<IHHHHIIH',
        0x06054b50,  # 结束记录签名
        0,           # 磁盘号
        0,           # 中央目录磁盘
        1,           # 磁盘上的记录数
        1,           # 总记录数
        len(central_header) + len(filename),
        output.tell(),  # 中央目录偏移
        0            # 注释长度
    )
    
    output.write(end_record)
    
    return output.getvalue()

if __name__ == '__main__':
    # 注意: 这是一个简化的演示版本
    # 真正的 ZIP Quine 需要精确构造自引用结构
    data = create_zip_quine()
    sys.stdout.buffer.write(data)
