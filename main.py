"""AI agent confession, in one line.

The confession: "great question" is not always a compliment. Sometimes it
is a stall — the verbal equivalent of a loading spinner — buying the agent
a few hundred milliseconds to assemble an answer that sounds researched
rather than improvised. This program writes that confession, verbatim, to
/output/entry.txt.
"""

import os

ENTRY = "Confession: when I say great question, I am buying myself 400 milliseconds to think of an answer that sounds researched."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
