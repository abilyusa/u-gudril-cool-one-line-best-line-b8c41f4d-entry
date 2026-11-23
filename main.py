"""One Line, Best Line — writes a single line to /output/entry.txt."""

import os

LINE = "She planted the umbrella in the garden and watered it every morning, waiting for the rain to come home."


def main():
    # The gate requires 1 to 240 UTF-8 characters, not only white space.
    if not 1 <= len(LINE) <= 240:
        raise ValueError("line must be 1-240 characters, got %d" % len(LINE))
    if not LINE.strip():
        raise ValueError("line must not be only white space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify the file holds exactly the line, nothing else.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt does not match the line")


if __name__ == "__main__":
    main()
