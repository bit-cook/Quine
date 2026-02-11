import pathlib


def main():
    here = pathlib.Path(__file__).resolve()
    names = ['py_chain_0.py', 'py_chain_1.py', 'py_chain_2.py']
    index = names.index(here.name)
    next_name = names[(index + 1) % len(names)]
    next_path = here.with_name(next_name)
    text = next_path.read_text(encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
