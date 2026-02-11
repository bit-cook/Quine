import pathlib
import sys


def load_chain(names=None, base=None):
    base = base or (pathlib.Path(__file__).parent.parent / "variants" / "ouroboros")
    if names is None:
        # default: detect py_chain_*.py files sorted by index
        names = sorted(
            [p.name for p in base.glob("py_chain_*.py")],
            key=lambda n: int(n.split("_")[-1].split(".")[0]),
        )
    files = [base / n for n in names]
    return files


def to_text(files):
    arrow = " → "
    names = [f.name for f in files]
    return arrow.join(names) + arrow + names[0]


def to_dot(files):
    names = [f.name for f in files]
    lines = ["digraph Ouroboros {", '  rankdir=LR;', '  node [shape=box];']
    for i, name in enumerate(names):
        nxt = names[(i + 1) % len(names)]
        lines.append(f'  "{name}" -> "{nxt}";')
    lines.append("}")
    return "\n".join(lines)


def main():
    args = sys.argv[1:]
    files = load_chain(args if args else None)
    print("Text view:")
    print("  " + to_text(files))
    print("\nGraphviz DOT:")
    print(to_dot(files))
    print("\nTip: Save DOT to a file and render with Graphviz `dot -Tpng file.dot -o chain.png`")


if __name__ == "__main__":
    main()

