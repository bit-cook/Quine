#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ASCII 艺术 Quine

源代码是一个 ASCII 艺术图案，输出也是相同的图案。
"""

# 图案定义
art = '''#!/usr/bin/env python3
"""
%s
"""

# 图案定义
art = %r

print(art %% (art.split(chr(10))[2], art))
'''

print(art % (art.split('\n')[2], art))
