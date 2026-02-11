import pathlib
import subprocess
import sys


def normalize(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def validate_chain(names):
    base = pathlib.Path(__file__).parent.parent / "variants" / "ouroboros"
    files = [base / name for name in names]
    for path in files:
        if not path.is_file():
            print(f"missing: {path}")
            return 1
    print("Ouroboros chain validation")
    print("=" * 60)
    all_ok = True
    for index, path in enumerate(files):
        next_path = files[(index + 1) % len(files)]
        expected = next_path.read_text(encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        out = normalize(result.stdout)
        ok = result.returncode == 0 and out == normalize(expected)
        status = "OK " if ok else "FAIL"
        print(f"{status} {path.name} → {next_path.name}")
        if not ok:
            all_ok = False
            if result.returncode != 0:
                print(result.stderr)
    return 0 if all_ok else 1


def main():
    default_chain = ["py_chain_0.py", "py_chain_1.py", "py_chain_2.py"]
    args = sys.argv[1:]
    names = args if args else default_chain
    code = validate_chain(names)
    sys.exit(code)


if __name__ == "__main__":
    main()

