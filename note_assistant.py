import argparse
from pathlib import Path


def main():
    # Check for note_assistant directory and create if necessary
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
        help="Add a tag to create specific directories to store a note under. Multi tags will result in each tag becoming the parent directory of the following tag",
    )
    parser.add_argument(
        "-s",
        "--subnote",
        action="append",
        help="Expand on ideas of a given note. This will add sub items under your original note. If your note does not exist it will be created.",
    )

    # Parse Args & Options
    args = parser.parse_args()

    note_assistant(args.note, args.directory, args.filename, args.tag, args.subnote)


def note_assistant(
    note, directory="note_assistant/notes", file_name="na", tags=None, subnotes=None
):
    """Function that will take a string and store as a note within a given markdown file."""

    # Check for any tags -- if they exist create a directory for each tag. Parent directories will be leftmost and child directories will be rightmost
    if tags:
        tags_path = ""
        for tag in tags:
            tags_path += f"{tag}/"
        path = Path.home() / Path(directory) / f"{tags_path}{file_name}.md"
    else:
        path = Path.home() / Path(directory) / f"{file_name}.md"
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a") as file:
        # Create formatted variable to add items as necessary
        formatted_note = f"# {note}\n"
        
        # Check for subnote options and add to formatted variable
        if subnotes:
            for sn in subnotes:
                formatted_note += f"- {sn}\n"
        
        # Write to note file
        file.write(formatted_note)


if __name__ == "__main__":
    main()
