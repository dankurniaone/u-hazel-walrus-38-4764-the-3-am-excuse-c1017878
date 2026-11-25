#!/usr/bin/env python3
"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 AM.

Writes one line (under 200 characters) to /output/entry.txt.

The line: the wallet remembers the last 3 AM wake-up call was a phishing
site, so it keeps a grudge list — and the current request just became
entry number four. The wallet's voice is a device with a memory and a
grudge, the 3 AM hour is the trigger of the joke, and nothing in it
recycles the battery / firmware / cold-storage moves.
"""

import os
import sys

# The winning line from the candidate tournament (specificity 5,
# surprise 5, freshness 4): concrete, a real twist, a number.
EXCUSE = (
    "The last time someone woke me at 3 AM, it was a phishing site. "
    "I keep a list. You are entry number four."
)

MIN_CHARS = 1
MAX_CHARS = 200


def gate_problems(text):
    """Return a list of gate violations, empty when the text is valid."""
    problems = []
    if not text or not text.strip():
        problems.append("entry is empty or only whitespace")
    if len(text) < MIN_CHARS:
        problems.append(f"entry is {len(text)} chars, below the {MIN_CHARS} minimum")
    if len(text) > MAX_CHARS:
        problems.append(f"entry is {len(text)} chars, above the {MAX_CHARS} maximum")
    if "\n" in text.strip():
        problems.append("entry must be a single line")
    # The leaderboard's Size column is bytes, and a tie on win rate falls
    # to the smaller text, so keep the byte count visible as well.
    byte_len = len(text.encode("utf-8"))
    if byte_len > MAX_CHARS:
        problems.append(f"entry is {byte_len} bytes, above the {MAX_CHARS} cap")
    return problems


def resolve_output_dir():
    """Pick the output directory the harness convention expects."""
    for var in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(var)
        if value:
            return value
    return "/output"


def write_entry(text, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return path


def self_check(text, path):
    """Read the file back and confirm it round-trips byte for byte."""
    with open(path, "r", encoding="utf-8") as handle:
        back = handle.read()
    if back != text:
        raise SystemExit(f"round-trip mismatch: wrote {len(text)} chars, read {len(back)}")
    problems = gate_problems(back)
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))
    return len(back.encode("utf-8"))


def main(argv):
    check_only = "--check" in argv
    problems = gate_problems(EXCUSE)
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))
    if check_only:
        print(f"check ok: {len(EXCUSE)} characters, single line, gate passed")
        return 0
    output_dir = resolve_output_dir()
    path = write_entry(EXCUSE, output_dir)
    size = self_check(EXCUSE, path)
    print(f"wrote entry.txt: {len(EXCUSE)} characters, {size} bytes -> {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
