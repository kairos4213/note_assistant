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

    path = form_file_path(directory, file_name, tags)

    # Convert subnotes to iterable list if None
    if subnotes is None:
        subnotes = []

    if contents := get_file(path, note, subnotes):
        lines = contents.splitlines(keepends=True)

        note_index = get_note_index(lines, note)
        if note_index >= 0:
            existing_subnotes = get_existing_subnotes(lines, note_index)
            # Add input subnotes to existing subnote list
            for subnote in subnotes:
                existing_subnotes.append(subnote)

            # Format and re-insert existing notes & input subnotes to lines
            lines.insert(note_index + 1, format_subnotes(existing_subnotes))

        # Add new note as well as any input subnotes to lines in file contents
        if note_index == -1:
            formatted_subnotes = format_subnotes(subnotes)
            formatted_note = format_note(note, formatted_subnotes)
            lines.append(formatted_note)

        # Rejoin lines and write to file
        updated_contents = "".join(lines)
        path.write_text(updated_contents)


def form_file_path(directory, file_name, tags):
    """Forms file path and makes any necessary directories"""

    # Check for any tags -- if they exist create a directory for each tag. Parent directories will be leftmost and child directories will be rightmost
    if tags:
        tags_path = ""
        for tag in tags:
            tags_path += f"{tag}/"
        path = Path.home() / Path(directory) / f"{tags_path}{file_name}.md"
    else:
        path = Path.home() / Path(directory) / f"{file_name}.md"

    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def get_file(file_path, note, subnotes):
    """Tries to read file path, if FileNotFound, write note & subnotes to disk"""

    try:
        return file_path.read_text()
    except FileNotFoundError:
        with file_path.open("w") as file:
            formatted_subnotes = format_subnotes(subnotes)
            formatted_note = format_note(note, formatted_subnotes)
            file.write(formatted_note)


def format_note(note, subnotes_string):
    """Takes a note and formatted subnote string and returns formatted note"""
    return f"# {note}\n" + subnotes_string


def format_subnotes(subnotes):
    """Takes list of subnotes and returns a formatted string"""
    formatted_subnotes_string = ""
    if subnotes:
        for subnote in subnotes:
            if subnote.startswith("\t-"):
                formatted_subnotes_string += subnote
            else:
                formatted_subnotes_string += f"\t- {subnote}\n"
    return formatted_subnotes_string


def get_note_index(lines, note):
    """Checks for existence of note in file and returns index if found, else -1"""
    for i in range(len(lines)):
        # If current line matches header (note):
        if lines[i] == f"# {note}\n":
            return i
    return -1


def get_existing_subnotes(lines, note_index):
    """Gets any existing subnotes under note and returns as list"""
    existing_subnotes = []
    subnote_index = note_index + 1

    # Start while loop if line is a subnote -- move all existing subnotes to list in memory
    while subnote_index < len(lines) and lines[subnote_index].startswith("\t-"):
        existing_subnotes.append(lines.pop(subnote_index))

    return existing_subnotes


if __name__ == "__main__":
    main()
