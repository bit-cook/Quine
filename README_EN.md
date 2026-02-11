# Quine - The Art of Self-Replication

> "A quine is a computer program which takes no input and produces a copy of its own source code as its only output."

## 📚 Introduction

Quine (named after philosopher Willard Van Orman Quine) is a computer program which takes no input and produces a copy of its own source code as its only output.
This project explores various implementations, variants, and theoretical aspects of Quines.

## 📁 Documentation Index

We provide extensive documentation to help you explore the world of Quines:

| File | Description |
|------|-------------|
| [THEORY.md](THEORY.md) | In-depth theoretical analysis (Kleene's Theorem, etc.) |
| [EXAMPLES.md](EXAMPLES.md) | Various Quine examples and explanations |
| [CHALLENGES.md](CHALLENGES.md) | Quine programming challenges |
| [FAQ.md](FAQ.md) | Frequently Asked Questions |
| [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) | Complete project summary |

## 🚀 Quick Start

### Verify a Quine (Python 3)

```bash
# Standard Python 3 Quine
python3 classic/quine.py | diff - classic/quine.py

# Minimal Version
python3 classic/quine_short.py | diff - classic/quine_short.py
```

## 📁 Project Structure

```
Quine/
├── README.md                    # Chinese Documentation
├── README_EN.md                 # This File
├── docs/                        # Documentation
├── classic/                     # Classic Implementations
├── variants/                    # Variants
├── generators/                  # Generators
├── tests_new/                   # Test Suite
└── tools/                       # Utilities
```

## 🎯 Core Principle

Quines rely on **Kleene's Recursion Theorem**.
A typical Quine consists of:
1.  **Data Section**: Represents the code.
2.  **Code Section**: Decodes and outputs the data.

## 📝 License

MIT License
