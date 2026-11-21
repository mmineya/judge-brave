from pathlib import Path


TEXT = (
    "Everyone is asleep. A loose button rests in the saucer by the bed. "
    "Its four holes are full of moonlight. In the next room, "
    "the clock finishes another minute."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
