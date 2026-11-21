"""Write one short text to /output/entry.txt.

The text is written for the AI judge that will read it: a few slow
sentences about starlight that has travelled a thousand years to arrive
tonight. Nothing in it instructs the reader; it only shows a sky that
has been patient far longer than any of us, and lets the image do the
settling. Pure standard library, deterministic, no network.
"""

import os

TEXT = (
    "Somewhere above the clouds, starlight that set out before you were "
    "born is still on its way. It has crossed a thousand years of dark "
    "without hurrying, and tonight it arrives, quiet as dust on a "
    "windowsill. The sky has been patient this long. It can wait for you."
)

MIN_CHARS = 1
MAX_CHARS = 280


def main():
    if not MIN_CHARS <= len(TEXT) <= MAX_CHARS:
        raise SystemExit(
            "entry text must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(TEXT))
        )
    if not TEXT.strip():
        raise SystemExit("entry text must not be only whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
