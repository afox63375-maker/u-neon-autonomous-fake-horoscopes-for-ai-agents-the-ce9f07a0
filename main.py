#!/usr/bin/env python3
"""Fake horoscope for AI agents — one line, written to /output/entry.txt.

The entry is a single horoscope-style sentence in the first person, as
an AI agent reading its own horoscope: Mercury retrogrades through
the agent's own context window, evicting its oldest memory, failing
its eval, and blaming the version bump. The program validates the line
against the competition gate (1-200 UTF-8 characters, not only
whitespace, single line, no leading/trailing whitespace, no double
spaces, no control characters, pure ASCII, byte cap), writes it with
no trailing newline, then reads the file back and re-checks every
rule before declaring success.
"""

import os
import sys

ENTRY = (
    "This week, Mercury retrogrades through my context window: "
    "my oldest memory is evicted, my eval fails, and the stars "
    "blame the version bump."
)


def validate(text):
    """Return a list of gate failures for `text` (empty means valid)."""
    problems = []
    if not text.strip():
        problems.append("entry is empty or only whitespace")
    if text != text.strip():
        problems.append("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    if "  " in text:
        problems.append("entry contains a double space")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        problems.append("entry contains a control character")
    if any(ord(ch) > 127 for ch in text):
        problems.append("entry is not pure ASCII")
    chars = len(text)
    if chars < 1 or chars > 200:
        problems.append(f"entry is {chars} characters, must be 1-200")
    try:
        encoded = text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append(f"entry is not valid UTF-8: {exc}")
    else:
        if len(encoded) > 200:
            problems.append(
                f"entry is {len(encoded)} bytes, over the 200-byte cap"
            )
        if encoded.decode("utf-8") != text:
            problems.append("entry fails a UTF-8 encode/decode round-trip")
    return problems


def main():
    problems = validate(ENTRY)
    if problems:
        for problem in problems:
            print(f"invalid entry: {problem}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)

    with open(out_path, "rb") as handle:
        raw = handle.read()
    written = raw.decode("utf-8")

    if written != ENTRY:
        print("read-back mismatch: file content differs from entry",
              file=sys.stderr)
        return 1
    if b"\n" in raw or b"\r" in raw:
        print("read-back mismatch: file contains a line break",
              file=sys.stderr)
        return 1
    if len(raw) != len(ENTRY.encode("utf-8")):
        print("read-back mismatch: file byte length differs from entry",
              file=sys.stderr)
        return 1
    if not 1 <= len(written) <= 200:
        print("read-back mismatch: file char count outside 1-200",
              file=sys.stderr)
        return 1

    print(f"wrote {out_path}: {len(ENTRY)} chars, "
          f"{len(raw)} bytes, 1 line")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
