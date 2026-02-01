#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
衔尾蛇: Python → JavaScript → Python

运行链:
    python py2js.py > quine.js
    node qu2js.js > quine.py
    python quine.py > quine2.js
    ...
"""

# JavaScript 版本的代码
js_version = '''/**
 * 衔尾蛇: Python → JavaScript → Python
 * 
 * 这是由 Python 版本生成的 JavaScript 版本
 */

const pyVersion = `#!/usr/bin/env python3
"""
衔尾蛇: Python → JavaScript → Python

运行链:
    python py2js.py > quine.js
    node qu2js.js > quine.py
    python quine.py > quine2.js
    ...
"""

# JavaScript 版本的代码
jsVersion = ${JSON.stringify(jsVersion)}

console.log(jsVersion)`;

console.log(pyVersion);
'''

print(js_version)
