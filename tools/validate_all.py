#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quine 主验证器 (Master Quine Validator)

一键验证仓库内所有 Quine 的正确性。它理解每种 Quine 的“类型”并采用相应判据：

  * self      : 运行后逐字节输出自身源代码
  * cycle     : A -> B -> A 的自包含 2-循环
  * chain     : 节点 i 输出节点 i+1 的衔尾蛇闭环
  * emitter   : 输出另一语言的、可独立验证的 Quine
  * multiquine: 同一文件在多种解释器下都输出自身
  * multiling : 编译型/脚本型多语言经典 Quine

用法:
    python tools/validate_all.py            # 验证全部
    python tools/validate_all.py -v         # 详细输出
    python tools/validate_all.py classic    # 只验证某目录/文件
"""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable


def _norm(s: str) -> str:
    return s.replace("\r\n", "\n").replace("\r", "\n")


def _read(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def run(cmd, cwd=None, stdin=None, timeout=30):
    return subprocess.run(cmd, cwd=cwd, input=stdin, capture_output=True,
                          text=True, timeout=timeout)


def have(tool):
    return shutil.which(tool) is not None


# ---------------------------------------------------------------------------
# Individual checks. Each returns (ok: bool, detail: str).
# ---------------------------------------------------------------------------

def check_self(path):
    orig = _norm(_read(path))
    out = _norm(run([PY, path]).stdout)
    if out == orig:
        return True, f"self-reproducing ({len(orig)} chars)"
    n = min(len(orig), len(out))
    i = 0
    while i < n and orig[i] == out[i]:
        i += 1
    return False, f"first diff @ {i}: orig={orig[i:i+25]!r} out={out[i:i+25]!r}"


def check_cycle(path):
    """A -> B -> A (self-contained 2-cycle)."""
    orig = _norm(_read(path))
    b = _norm(run([PY, path]).stdout)
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False,
                                     encoding="utf-8") as f:
        f.write(b)
        bpath = f.name
    try:
        a2 = _norm(run([PY, bpath]).stdout)
    finally:
        os.unlink(bpath)
    if b == orig:
        return False, "not a cycle: output equals source (it is a self-quine)"
    if a2 == orig:
        return True, "A -> B -> A closed"
    return False, "cycle did not return to A"


def check_chain(paths):
    """Each node outputs the next; last wraps to first."""
    srcs = [_norm(_read(p)) for p in paths]
    for i, p in enumerate(paths):
        out = _norm(run([PY, p]).stdout)
        nxt = srcs[(i + 1) % len(paths)]
        if out != nxt:
            return False, f"{os.path.basename(p)} did not output next node"
    return True, f"{len(paths)}-node closed loop"


def check_emitter_py2js(path):
    """py2js.py emits a JS quine; verify the emitted JS with node."""
    if not have("node"):
        return None, "node not available (skipped)"
    js = run([PY, path]).stdout
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False,
                                     encoding="utf-8") as f:
        f.write(js)
        jspath = f.name
    try:
        out = run(["node", jspath]).stdout
    finally:
        os.unlink(jspath)
    if _norm(out) == _norm(js):
        return True, "emits a valid JavaScript quine"
    return False, "emitted JS is not a quine"


def check_multiling(path):
    ext = os.path.splitext(path)[1].lower()
    orig = _norm(_read(path))
    tmp = tempfile.mkdtemp()
    try:
        if ext == ".c":
            if not have("gcc"):
                return None, "gcc not available (skipped)"
            exe = os.path.join(tmp, "q")
            r = run(["gcc", "-o", exe, path])
            if r.returncode != 0:
                return False, "compile failed: " + r.stderr.strip()[:120]
            out = run([exe]).stdout
        elif ext == ".rs":
            if not have("rustc"):
                return None, "rustc not available (skipped)"
            exe = os.path.join(tmp, "q")
            r = run(["rustc", "-O", "-o", exe, path])
            if r.returncode != 0:
                return False, "compile failed: " + r.stderr.strip()[:120]
            out = run([exe]).stdout
        elif ext == ".go":
            if not have("go"):
                return None, "go not available (skipped)"
            out = run(["go", "run", path], cwd=os.path.dirname(path)).stdout
        elif ext == ".java":
            if not have("javac") or not have("java"):
                return None, "java not available (skipped)"
            r = run(["javac", path], cwd=os.path.dirname(path))
            if r.returncode != 0:
                return False, "compile failed: " + r.stderr.strip()[:120]
            cls = os.path.splitext(os.path.basename(path))[0]
            out = run(["java", "-cp", os.path.dirname(path), cls]).stdout
        elif ext == ".js":
            if not have("node"):
                return None, "node not available (skipped)"
            out = run(["node", path]).stdout
        elif ext == ".sh":
            if not have("bash"):
                return None, "bash not available (skipped)"
            out = run(["bash", path]).stdout
        else:
            return None, f"unsupported ext {ext} (skipped)"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    if _norm(out) == orig:
        return True, "self-reproducing"
    return False, "output != source"


def check_brainfuck(path):
    """Verify a brainfuck quine with a tiny built-in interpreter."""
    with open(path, encoding="utf-8") as f:
        code = f.read()
    tape = [0] * 100000
    ptr = 0
    out = []
    i = 0
    steps = 0
    stack = []
    match = {}
    for idx, c in enumerate(code):
        if c == "[":
            stack.append(idx)
        elif c == "]":
            j = stack.pop()
            match[j] = idx
            match[idx] = j
    while i < len(code):
        c = code[i]
        if c == "+":
            tape[ptr] = (tape[ptr] + 1) & 255
        elif c == "-":
            tape[ptr] = (tape[ptr] - 1) & 255
        elif c == ">":
            ptr += 1
        elif c == "<":
            ptr -= 1
        elif c == ".":
            out.append(chr(tape[ptr]))
        elif c == "[":
            if tape[ptr] == 0:
                i = match[i]
        elif c == "]":
            if tape[ptr] != 0:
                i = match[i]
        i += 1
        steps += 1
        if steps > 500_000_000:
            return False, "brainfuck step limit exceeded"
    produced = "".join(out)
    if produced == code:
        return True, "brainfuck quine ({} bytes)".format(len(code))
    return False, "output != source"


def check_generator(path):
    """Run the generator, then verify its output is a valid quine."""
    r = run([PY, path])
    if r.returncode != 0:
        return False, "generator errored: " + r.stderr.strip()[:120]
    produced = r.stdout
    if not produced.strip():
        return False, "generator produced no output"
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False,
                                     encoding="utf-8") as f:
        f.write(produced)
        ppath = f.name
    try:
        out = run([PY, ppath]).stdout
    finally:
        os.unlink(ppath)
    if _norm(out) == _norm(produced):
        return True, "produces a valid quine"
    return False, "generated program is not a quine"


def check_meta_quine(path):
    """meta_quine -> generator -> quine (two-stage chain)."""
    r = run([PY, path])
    if r.returncode != 0:
        return False, "meta errored: " + r.stderr.strip()[:120]
    generator_src = r.stdout
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False,
                                     encoding="utf-8") as f:
        f.write(generator_src)
        gpath = f.name
    try:
        r2 = run([PY, gpath])
        quine_src = r2.stdout
    finally:
        os.unlink(gpath)
    if not quine_src.strip():
        return False, "generated generator produced no quine"
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False,
                                     encoding="utf-8") as f:
        f.write(quine_src)
        qpath = f.name
    try:
        out = run([PY, qpath]).stdout
    finally:
        os.unlink(qpath)
    if _norm(out) == _norm(quine_src):
        return True, "meta -> generator -> quine chain valid"
    return False, "final quine not self-reproducing"


# ---------------------------------------------------------------------------
# Registry: maps relative paths to (kind, callable)
# ---------------------------------------------------------------------------

def build_registry():
    reg = {}  # relpath -> (kind, fn)

    def add(rel, kind, fn):
        reg[rel] = (kind, fn)

    # self-quines (Python)
    for rel in [
        "classic/quine.py", "classic/quine_short.py",
        "variants/multiquine.py",
        "artistic/ascii_art_quine.py", "artistic/game_of_life_quine.py",
        "artistic/musical_quine.py", "artistic/qr_quine.py",
        "variants/palindrome_quine.py",
        "python2/quine_py2_compat.py",
    ]:
        add(rel, "self", check_self)

    # 2-cycles
    for rel in ["variants/iterative_quine.py",
                "variants/ouroboros/python2python3.py"]:
        add(rel, "cycle", check_cycle)

    # emitter
    add("variants/ouroboros/py2js.py", "emitter", check_emitter_py2js)

    # brainfuck
    add("esoteric/quine.bf", "brainfuck", check_brainfuck)

    # multi-language classics
    for rel in ["classic/quine.c", "classic/quine.go", "classic/quine.java",
                "classic/quine.rs", "classic/quine.js", "esoteric/quine.sh"]:
        add(rel, "multiling", check_multiling)

    # generators
    add("generators/quine_generator.py", "generator", check_generator)
    add("generators/meta_quine.py", "meta", check_meta_quine)

    return reg


def discover_chain():
    base = os.path.join(ROOT, "variants", "ouroboros")
    names = sorted(
        (f for f in os.listdir(base) if f.startswith("py_chain_") and f.endswith(".py")),
        key=lambda n: int(n.split("_")[-1].split(".")[0]),
    )
    return [os.path.join(base, n) for n in names]


def main():
    ap = argparse.ArgumentParser(description="Quine 主验证器")
    ap.add_argument("target", nargs="?", help="只验证某目录或文件")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    reg = build_registry()
    results = []  # (label, kind, ok(None=skip), detail)

    def consider(rel, kind, fn):
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            return
        if args.target:
            t = args.target.rstrip("/")
            if not (rel == t or rel.startswith(t + "/") or os.path.basename(rel) == t):
                return
        ok, detail = fn(path)
        results.append((rel, kind, ok, detail))

    for rel, (kind, fn) in reg.items():
        consider(rel, kind, fn)

    # chain (unless a specific non-chain target was given)
    chain = discover_chain()
    if chain and (not args.target or "ouroboros" in args.target or "py_chain" in args.target):
        ok, detail = check_chain(chain)
        results.append(("variants/ouroboros/py_chain_*.py", "chain", ok, detail))

    # Report
    print("=" * 66)
    print("Quine Master Validator")
    print("=" * 66)
    passed = failed = skipped = 0
    for rel, kind, ok, detail in sorted(results):
        if ok is None:
            status = "SKIP"
            skipped += 1
        elif ok:
            status = "PASS"
            passed += 1
        else:
            status = "FAIL"
            failed += 1
        print(f"[{status}] {kind:9s} {rel}")
        if args.verbose or status == "FAIL":
            print(f"         -> {detail}")

    print("-" * 66)
    print(f"PASS {passed} | FAIL {failed} | SKIP {skipped}")
    print("=" * 66)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
