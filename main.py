"""The 3 AM Excuse — make.fun entry.

Writes one line to /output/entry.txt: a hardware wallet refusing to sign at 3 AM.
Gate: UTF-8, 1-200 chars. The line is 107 chars, 93 spare.
Tournament winner: dog token no longer exists, 5/5/5.
"""
import sys
from pathlib import Path

LINE = "The last time I signed at 3 AM, you bought a token named after a dog that no longer exists. I have learned."

CANDIDATES = [
    ("The sun is up, the birds are loud, and I refuse to sign before coffee.", 3, 3, 3),
    ("Bear markets I can handle. A memecoin vault at 3 AM is where I draw the line.", 5, 4, 4),
    ("The last time I signed at 3 AM, you bought a token named after a dog that no longer exists. I have learned.", 5, 5, 5),
    ("I am a cold wallet. Right now I am even colder. Come back at noon.", 3, 3, 2),
    ("My seed phrase is 'yes'. I am not telling you the rest at 3 AM.", 5, 4, 5),
    ("Seven transactions at 3 AM, all of them yours, none of them sober.", 5, 5, 4),
    ("The blockchain never sleeps, but I do, and so should you.", 3, 3, 3),
]

def main(argv):
    if "--check" in argv:
        n = len(LINE)
        print(f"VALID: {n} chars, {len(LINE.split())} words, {200 - n} spare under the 200-char gate")
        return 0
    if "--self-test" in argv:
        out = Path("/tmp/3am-excuse-self-test.txt")
        out.write_text(LINE + "\n", encoding="utf-8")
        again = out.read_text(encoding="utf-8")
        assert again == LINE + "\n"
        print("self-test: byte-identical")
        return 0
    if "--tournament" in argv:
        for text, spec, surp, fresh in CANDIDATES:
            mark = " <-- winner" if text == LINE else ""
            print(f"{spec + surp + fresh:2d}  ({spec}/{surp}/{fresh})  {text}{mark}")
        return 0
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} chars to {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
