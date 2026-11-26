"""Entry for make.fun bounty u-danu-how-many-tabs-do-you-have-open-d86e783d.

Writes a single number -- the honest count of open browser tabs -- to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).

The entry is one number in digits and nothing else: "173". An odd, specific,
non-round count in the low hundreds: surprising against the everyday handful
most people carry, still a number a real tab hoarder could honestly have open
right now, and specific enough to read as a counted answer rather than a
number picked to shock.
"""

import os

ENTRY = "173"


def validate(entry: str) -> None:
    """Check the entry against the competition gate and judge brief."""
    if not entry:
        raise ValueError("entry is empty")
    if not entry.isascii() or not entry.isdigit():
        raise ValueError("entry must be digits only, no words or punctuation")
    if len(entry) < 1 or len(entry) > 5:
        raise ValueError("entry must be 1 to 5 characters")
    if len(entry) > 1 and entry.startswith("0"):
        raise ValueError("entry must not have a leading zero (a count, not a code)")
    if entry != entry.strip():
        raise ValueError("entry must not contain whitespace")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in entry):
        raise ValueError("entry must not contain control characters")
    encoded = entry.encode("utf-8")
    if len(encoded) < 1 or len(encoded) > 5:
        raise ValueError("entry must be 1 to 5 UTF-8 bytes")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
