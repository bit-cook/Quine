# Quine - The Art of Self-Replication

[中文文档 (Chinese README)](README.md)

> **Quine** is a self-replicating program that reconstructs its own source code during execution without any external input. It is a direct manifestation of "fixed points" in computability theory, demonstrating how code can reproduce itself like a living organism.

## 📚 Overview

The notion of a **quine** (self-reproducing program) comes from computability theory and is named after the philosopher and logician **Willard Van Orman Quine** (1908–2000).  
The term “quine” was popularized by Douglas Hofstadter in *Gödel, Escher, Bach* to describe programs that output their own source code.

This repository systematically explores different implementations and variants of Quines, from minimal Python examples to multilingual Ouroboros chains.

## 🎯 Core Principles

Quines are not ad‑hoc tricks; their existence follows directly from **Kleene’s Recursion Theorem** (a fixed‑point theorem) in computability theory.  
Roughly speaking, it guarantees that in any Turing‑complete language there exists a program that can reproduce its own description.

A typical quine can be viewed as having two conceptual parts:

1.  **Code part** – the logic that prints.
2.  **Data part** – a textual representation of (part of) the program itself, usually stored as a string.

Execution pattern:

> Use the data part to reconstruct and print the code part, while also printing the data itself.

Classic structural pattern:

```text
Program = Data + code(Data → "Data + code(Data)")
```

## 📖 Classic Examples

### Python 3 Minimal Quine (29 chars)

```python
_='_=%r;print(_%%_)';print(_%_)
```

### Python 3 Standard Version (with comments)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 3 Quine
"""
s='s=%r;print(s%%s)';print(s%s)
```

### Python 2/3 Compatible Version

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
s="s=%r;print(s%%s)"
print(s%s)
```

## 🚀 Quick Start

### 1. Verifying a Quine

The most direct way to verify a quine is to redirect its output and compare it to its own source file.

```bash
# Standard Python 3 implementation
python3 classic/quine.py | diff - classic/quine.py

# Minimal version
python3 classic/quine_short.py | diff - classic/quine_short.py

# If diff produces no output, the quine is valid.
```

### 2. Run the Demo

We provide a demo script that runs and checks multiple quine variants:

```bash
python3 demo.py
```

### 3. Explore the Enhanced Variant

This project also experiments with an “engineering‑oriented” quine that introduces configuration and plugin mechanisms:

```bash
python3 enhanced_quine.py
```

## 🗺️ Learning Roadmap

This repository is packed with content. We recommend the following path:

1.  **👀 Start Here (Level 0)**:
    *   Run `python3 demo.py` to see "programs printing themselves" in action.
    *   Read the "Core Principles" section in this README.

2.  **👶 Beginner (Level 1)**:
    *   Read "Level 1" and "Level 2" in [EXAMPLES.md](EXAMPLES.md) to understand the basic Code + Data structure.
    *   Try running `classic/quine.py` and modifying it to see what happens.

3.  **🧑‍💻 Intermediate (Level 2)**:
    *   Read [THEORY.md](THEORY.md) to learn about Kleene's Recursion Theorem.
    *   Complete the first 3 challenges in [CHALLENGES.md](CHALLENGES.md).
    *   Experiment with `variants/iterative_quine.py` (A→B→A cycle).

4.  **🚀 Advanced (Level 3)**:
    *   Explore `variants/ouroboros/` and use the generator to create your own N-node self-referential chains.
    *   Study `variants/multiquine.py` to understand polyglot techniques.
    *   Use the validators and visualizers in `tools/` for your research.

## ✨ Features

This repository is intended as a **quine lab**, not just a code snippet collection:

- **Multi‑language implementations**: Classic quines in Python, C, Go, Java, Rust, JavaScript, etc.
- **Variant exploration**: Iterative quines (A→B→A), Ouroboros chains, multilingual forms, and more.
- **Engineering experiments**: Configuration management via `config.json` and a simple plugin system under `plugins/` (see `enhanced_quine.py`).
- **Quality assurance**: Automated tests in `tests_new/` and CI/CD configuration to keep self‑reproduction strict and reliable.

## 📂 Project Structure

```text
Quine/
├── README.md               # Chinese main README
├── README_EN.md            # This English README
├── demo.py                 # Integrated demonstration script
├── enhanced_quine.py       # Enhanced quine with config/plugins
├── config.json             # Configuration file
├── classic/                # Classic implementations (Python, C, etc.)
├── variants/               # Variants (iterative, Ouroboros, etc.)
├── generators/             # Quine generators
├── artistic/               # Artistic quines (ASCII art, QR code, etc.)
├── esoteric/               # Esoteric language quines (Brainfuck, ...)
├── plugins/                # Plugin system experiments
├── tests_new/              # Automated test suite
└── tools/                  # Utilities (validator, size optimizer, visualizer)
```

## 🐍 Python Versions

### Python 3 (Recommended)

- **Locations**: `classic/`, `generators/`, `tests/`, `tools/`, `variants/`, `artistic/`
- **Highlights**: Modern syntax, type hints, f‑strings.
- **Usage**: `python3 <file>`

### Python 2.7 (Compatibility Only)

- **Location**: `python2/`
- **Note**: Python 2 reached end‑of‑life in 2020; kept here purely for historical/compatibility reasons.
- **Usage**: `python python2/<file>`

## 🎨 Variant Types

### 1. Iterative Quine

Program A outputs program B, B outputs C, C outputs A, forming a cycle.

### 2. Multiquine (Multilingual Quine)

A single source file is interpreted correctly as a quine in multiple programming languages.

### 3. Ouroboros Chain

Program A outputs the source of B, B outputs C, …, and the last program outputs A, forming a closed “Ouroboros” loop.

## 🔬 Advanced: Ouroboros Chain Toolkit

The repository includes a small toolkit around Ouroboros chains, so you can move from the concept to concrete, verifiable experiments:

- **Generate Python chains of arbitrary length**  
  In `variants/ouroboros/`, use the generator to create an N‑node cycle:

  ```bash
  # Generate a 3‑node chain: py_chain_0.py, py_chain_1.py, py_chain_2.py
  python variants/ouroboros/make_py_chain.py 3
  ```

- **Automatically validate the closed loop**  
  Use the validator to check that each node prints the exact source of the next node:

  ```bash
  python tools/ouroboros_validator.py
  ```

- **Visualize the chain structure**  
  Get both a text view and a Graphviz DOT description:

  ```bash
  python tools/ouroboros_visualizer.py
  ```

  Save the DOT output and render it with Graphviz, for example:

  ```bash
  python tools/ouroboros_visualizer.py > chain.dot
  dot -Tpng chain.dot -o chain.png
  ```

For the theoretical background and detailed walkthroughs, see:

- Level 5 “Ouroboros chain” and the advanced example section in `EXAMPLES.md`
- Section 5.3 “Ouroboros chains and multi‑step fixed points” in `THEORY.md`

## 🧪 Coding Challenges

The repository also includes a series of quine‑related programming challenges:

1. **Shortest quine** – Minimize character count in a given language.
2. **Iterative quine** – Build cycles of length ≥ 2.
3. **Multiquine** – Make one file act as a quine in multiple languages.
4. **Radiation‑hardened quine** – Error‑tolerant or noise‑resistant variants.

See `CHALLENGES.md` for the full list and details.

## 📝 Documentation Index

To support deeper understanding, we provide several documents:

| File | Description |
|------|-------------|
| [THEORY.md](THEORY.md) | Theoretical foundations (fixed‑point theorems, Kleene’s recursion theorem, etc.) |
| [EXAMPLES.md](EXAMPLES.md) | Worked examples of quines in various languages |
| [CHALLENGES.md](CHALLENGES.md) | 25+ quine‑related coding challenges |
| [FAQ.md](FAQ.md) | Frequently asked questions about definitions, tricks, and edge cases |
| [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) | High‑level summary of the repository structure and content |
| [FIXES_REPORT.md](FIXES_REPORT.md) | Historical bug‑fix and change notes |

## 🔗 Related Resources

- [Wikipedia – Quine (computing)](https://en.wikipedia.org/wiki/Quine_(computing))
- [Wikipedia – Quine's paradox](https://en.wikipedia.org/wiki/Quine%27s_paradox)
- [Rosetta Code – Quine](https://rosettacode.org/wiki/Quine)

## 📝 License

MIT License

---

> "Yields falsehood when preceded by its quotation" yields falsehood when preceded by its quotation.
>
> "‘在其引用之后产生谬误’在其引用之后产生谬误。"
>
> -- Quine's Paradox (奎因悖论)
