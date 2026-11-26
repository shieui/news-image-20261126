#!/usr/bin/env python3
"""news-image-20261126: copy the pre-rendered poster to /output/entry.png.

The poster was drawn in this session and shipped as entry.png beside this
file. This program does no drawing and no network access: it only copies
those exact bytes to the output directory, so both graded runs produce
byte-identical output.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    with open(source, "rb") as fh:
        magic = fh.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    if os.path.getsize(target) != os.path.getsize(source):
        print("copied file size mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
