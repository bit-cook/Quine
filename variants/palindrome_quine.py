#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
回文 Quine 尝试

回文 Quine 极其困难，因为代码需要对称且能输出自身。
这是一个近似实现 - 它输出自身，但严格来说不是回文。

真正的回文 Quine 需要语言支持非常灵活的语法。
"""

s = 's = %r;print(s %% s)'#';(s %% s)tnirp;]r% = s'
print(s % s)
