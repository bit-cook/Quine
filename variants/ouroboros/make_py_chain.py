import sys
import pathlib


TEMPLATE = """import pathlib


def main():
    here = pathlib.Path(__file__).resolve()
    names = {names}
    index = names.index(here.name)
    next_name = names[(index + 1) % len(names)]
    next_path = here.with_name(next_name)
    text = next_path.read_text(encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
"""


def generate(count, prefix="py_chain_"):
    if count < 2:
        raise ValueError("count must be at least 2")
    base = pathlib.Path(__file__).parent
    names = [f"{prefix}{i}.py" for i in range(count)]
    for name in names:
        path = base / name
        code = TEMPLATE.format(names=repr(names))
        path.write_text(code, encoding="utf-8")
        print(f"Generated: {name}")
    print(f"Successfully generated chain of {count} files in {base}")


def main():
    if len(sys.argv) < 2:
        print("usage: python make_py_chain.py <count> [prefix]")
        sys.exit(1)
    count = int(sys.argv[1])
    prefix = sys.argv[2] if len(sys.argv) > 2 else "py_chain_"
    generate(count, prefix)


if __name__ == "__main__":
    main()

