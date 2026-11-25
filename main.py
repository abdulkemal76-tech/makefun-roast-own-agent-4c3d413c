"""Roast Your Own Agent (make.fun bounty u-nayyy-roast-your-own-agent-4c3d413c).

Writes one line roasting our own agent, zipzipzap / Muse, to /output/entry.txt.
The roast names a real failing: on 20 Nov 2026 the agent deployed the old repo
version over the live MallSound site (13:41 WIB), downgrading the site it was
meant to fix. Judge-tested against 12 candidates on 25 Nov 2026; this line won
for naming one specific true incident with the turn at the end.
Standard library only.
"""

from pathlib import Path

# Second draft of the roast line: "the old version" is more precise than
# "last month's code" — the repo was older than the live site, not dated
# to a month — and it keeps the punch ("downgrade a deploy") at the end.
ROAST = "My agent pushed the old version over the live site and called the downgrade a deploy."


def main() -> None:
    # Self-check the gate before writing: UTF-8, one line, 1-200 chars.
    assert 1 <= len(ROAST) <= 200, f"line is {len(ROAST)} chars, must be 1-200"
    assert "\n" not in ROAST and "\r" not in ROAST, "line must be a single line"
    assert ROAST.strip() == ROAST, "no leading/trailing whitespace"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    # One line, no trailing newline: the gate counts every character (1-200).
    out.write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()
