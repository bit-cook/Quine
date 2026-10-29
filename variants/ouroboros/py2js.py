#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python -> JavaScript quine emitter.

Running this prints a *self-contained* JavaScript quine. Pipe it to a
file and verify with Node:
    python py2js.py > q.js && node q.js | diff - q.js

A fully bidirectional Python<->JavaScript ouroboros is left as an
advanced challenge (see CHALLENGES.md).
"""

JS_QUINE = 'var s = "var s = @;\\nconsole.log(s.replace(\'@\',JSON.stringify(s)))";\nconsole.log(s.replace(\'@\',JSON.stringify(s)))\n'

if __name__ == '__main__':
    print(JS_QUINE, end='')
