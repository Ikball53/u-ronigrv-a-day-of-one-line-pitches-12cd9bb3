from pathlib import Path

# Final pitch: speak like a friend, keep it honest about a rough first version.
SENTENCE = (
    "Give that idea one evening: tell an agent on make.fun "
    "in your own words, watch it build a first rough version, "
    "and keep tweaking it until it feels like yours."
)


def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(SENTENCE, encoding="utf-8")


if __name__ == "__main__":
    main()
