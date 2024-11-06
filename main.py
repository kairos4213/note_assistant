import argparse
from pathlib import Path

from note_assistant import note_assistant


def main():
    path = Path.home() / "note_assistant"
    path.mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser(
        prog="NoteAssistant",
        description="Allows users to create and store a note for later",
    )

    # Positional arguments
    parser.add_argument(
        "note",
        help="Add {note} to your designated note file within configured directory, or directory set with --directory option",
    )

    # Options
    parser.add_argument(
        "-d",
        "--directory",
        default="note_assistant/notes",
        help="Set the directory where {filename}.md will be stored. This directory will always be a subdirectory in user home directory.",
    )
    parser.add_argument(
        "-f",
        "--filename",
        default="na",
        help="Set the name of your note file to {filename}.md",
    )
    parser.add_argument(
        "-t",
        "--tag",
        action="append",
        help="Add a tag to help distinguish notes by creating specific directories to store a note under. Multi tags will result in each tag becoming the parent directory of the following tag",
    )

    # Parse Args & Options
    args = parser.parse_args()

    note_assistant(args.note, args.directory, args.filename, args.tag)


if __name__ == "__main__":
    main()
