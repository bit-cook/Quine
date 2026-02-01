#!/bin/bash
# Shell Quine

# 方法1: 使用 $0 读取自身
# cat "$0"

# 方法2: 真正的 Quine (不读取文件)
s='s=%s%s%s;printf "$s" "\'" "$s" "\'"
printf "$s" "'" "$s" "'"

# 验证: bash quine.sh | diff - quine.sh
