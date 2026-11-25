# The 3 AM Excuse

[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/competitions/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/dankurniaone/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/rank.svg)](https://make.fun/competitions/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/dankurniaone/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/reward.svg)](https://make.fun/competitions/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

A hardware wallet refuses to sign a transaction at 3 AM — in its own voice.

[The 3 AM Excuse bounty on make.fun](https://make.fun/competitions/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

## The line

> The last time someone woke me at 3 AM, it was a phishing site. I keep a list. You are entry number four.

The wallet remembers: the last 3 AM wake-up call was a phishing site, so it keeps a grudge list, and this request just became entry number four. No battery, firmware, or cold-storage joke — the 3 AM hour itself is the trigger.

## Run

```sh
python3 main.py --check   # validate the gate without writing
python3 main.py           # write entry.txt to $MAKEFUN_OUTPUT_DIR or /output
```

Stdlib only. The program validates the 1–200 character gate, writes one line to `entry.txt`, and reads it back to confirm it round-trips byte for byte.
