#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quine 核心测试套件 (unittest)

复用 tools/validate_all.py 的判据，对仓库内所有 Quine 做类型感知的严格验证。
在 CI 与本地均可运行:

    python -m unittest discover -s tests_new -v
    python tests_new/test_core.py
"""

import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "tools"))

import validate_all as V  # noqa: E402


def rel(*parts):
    return os.path.join(ROOT, *parts)


SELF_QUINES = [
    "classic/quine.py",
    "classic/quine_short.py",
    "variants/multiquine.py",
    "variants/palindrome_quine.py",
    "python2/quine_py2_compat.py",
    "artistic/ascii_art_quine.py",
    "artistic/game_of_life_quine.py",
    "artistic/musical_quine.py",
    "artistic/qr_quine.py",
]

CYCLES = [
    "variants/iterative_quine.py",
    "variants/ouroboros/python2python3.py",
]


class TestSelfQuines(unittest.TestCase):
    pass


def _make_self_test(r):
    def test(self):
        ok, detail = V.check_self(rel(r))
        self.assertTrue(ok, f"{r}: {detail}")
    return test


for _r in SELF_QUINES:
    setattr(TestSelfQuines, "test_" + _r.replace("/", "_").replace(".", "_"),
            _make_self_test(_r))


class TestCycles(unittest.TestCase):
    pass


def _make_cycle_test(r):
    def test(self):
        ok, detail = V.check_cycle(rel(r))
        self.assertTrue(ok, f"{r}: {detail}")
    return test


for _r in CYCLES:
    setattr(TestCycles, "test_" + _r.replace("/", "_").replace(".", "_"),
            _make_cycle_test(_r))


class TestOuroborosChain(unittest.TestCase):
    def test_chain_closed_loop(self):
        chain = V.discover_chain()
        if not chain:
            self.skipTest("no py_chain_* files present")
        ok, detail = V.check_chain(chain)
        self.assertTrue(ok, detail)


class TestEmitter(unittest.TestCase):
    def test_py2js_emits_js_quine(self):
        ok, detail = V.check_emitter_py2js(rel("variants/ouroboros/py2js.py"))
        if ok is None:
            self.skipTest(detail)
        self.assertTrue(ok, detail)


class TestGenerators(unittest.TestCase):
    def test_quine_generator(self):
        ok, detail = V.check_generator(rel("generators/quine_generator.py"))
        self.assertTrue(ok, detail)

    def test_meta_quine(self):
        ok, detail = V.check_meta_quine(rel("generators/meta_quine.py"))
        self.assertTrue(ok, detail)


if __name__ == "__main__":
    unittest.main(verbosity=2)
