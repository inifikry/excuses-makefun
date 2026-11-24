#!/usr/bin/env python3
"""Two Days of Excuses — writes one funny AI excuse to /output/entry.txt.

Deterministic: every run writes the exact same single line, with no
trailing newline, so the file is exactly the line itself.
"""

LINE = "I was 99% confident I'd finish on time. That confidence was the only thing I shipped."

# Self-check against the gate: 1-200 UTF-8 characters, one line, not blank.
assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
assert "\n" not in LINE and LINE.strip() == LINE, "line must be a single non-blank line"


def main():
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
