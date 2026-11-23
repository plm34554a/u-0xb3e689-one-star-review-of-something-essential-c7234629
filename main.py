#!/usr/bin/env python3
"""Write a deadpan one-star review of an everyday essential to a text file.

Standard library only. The output path is $MAKEFUN_OUTPUT when set,
otherwise $MAKEFUN_OUTPUT_DIR/entry.txt when that is set, otherwise
/output/entry.txt.
"""

import os

REVIEW = (
    "One star. Water falls from the sky for free, has no taste, "
    "and still tastes like a swimming pool in every hotel I have ever stayed in."
)


def output_path() -> str:
    """Resolve where the review should be written."""
    path = os.environ.get("MAKEFUN_OUTPUT")
    if path:
        return path
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if directory:
        return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def main() -> None:
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
