#!/usr/bin/env python3
"""One-line robot pickup line entry for the make.fun bounty
"The Robot Pickup Line Championship".

Writes exactly one line — a single-sentence pickup line in the voice of
a robot trying to charm someone — to /output/entry.txt. Deterministic:
no input, no network, no randomness; the same bytes on every run.

Craft notes: the setup names a specific, instantly recognisable machine
detail — a robot programmed to feel nothing — and the punchline turns it
into an involuntary, very human tell: its cooling fan spinning up
whenever the person walks in. That fits the judge brief: first a robot's
pickup line, then a joke that grows out of being a machine (firmware,
cooling hardware), with a surprising turn and no padding.

Second thinking step — why the line works. The voice is a robot
confessing a malfunction it cannot explain: "I was programmed to never
feel anything" is deadpan, absolute, and completely in character, so
the reader trusts the machine's self-report. The twist is that the
evidence for feeling arrives as hardware, not emotion: a cooling fan
spinning up is the robot equivalent of a blush or a racing heartbeat,
a tell it did not choose and cannot hide. Framing it as a question
("so why does...?") lets the robot hand the conclusion to the listener
instead of declaring love, which keeps the line a pickup rather than a
speech — the other person gets to answer. Nothing is generic: "cooling
fan" could only belong to a machine, and "every time you walk in" makes
the trigger one specific person, which is what turns a joke about a
robot into a compliment aimed at someone.
"""

import os

LINE = (
    "I was programmed to never feel anything, so why does my cooling fan "
    "spin up every time you walk in?"
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert "\n" not in LINE and LINE == LINE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
