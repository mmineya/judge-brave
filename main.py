from pathlib import Path


TEXT = (
    "The kettle clicks off. A last thread of steam unwinds above the chipped blue cup. "
    "Rain darkens the doorstep. The door stands open an inch, and the small brass "
    "hinge holds steady between the room and the rain."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
