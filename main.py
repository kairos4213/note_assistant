import argparse
from pathlib import Path

from note_assistant import note_assistant


def main():
    path = Path.home() / "note_assistant"
    path.mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser()

    # Positional arguments
    parser.add_argument("note", help="add {note} to your designated note file")

    # Options
    parser.add_argument(
        "-d",
        "--directory",
        default="note_assistant/notes",
        help="set the directory where note.md will be stored",
    )
    parser.add_argument(
        "-f", "--filename", default="na", help="set name of note file to {filename}.md"
    )

    # Parse Args & Options
    args = parser.parse_args()

    note_assistant(args.note, args.directory, args.filename)


if __name__ == "__main__":
    main()
