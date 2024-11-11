from pathlib import Path


def note_assistant(
    note, directory="note_assistant/notes", file_name="na", tags=None, subnotes=None
):
    """Function that will take a string and store as a note within a given markdown file."""

    path = form_file_path(directory, file_name, tags)

    if contents := get_file(path, note, subnotes):
        if subnotes is None:
            subnotes = []
        updated_contents = update_and_format_file(contents, note, subnotes)
        path.write_text(updated_contents)


def form_file_path(directory, file_name, tags):
    """Forms file path and makes any necessary directories"""

    # Check for any tags -- if they exist create a directory for each tag.
    # Parent directories will be leftmost and child directories will be
    #  rightmost
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
    """Tries to read file path, if FileNotFound, write note/subnotes to file"""

    try:
        return file_path.read_text()
    except FileNotFoundError:
        with file_path.open("w") as file:
            formatted_subnotes = format_subnotes(subnotes)
            formatted_note = format_note(note, formatted_subnotes)
            file.write(formatted_note)


def update_and_format_file(contents, note, subnotes):
    """Returns formatted note with any provided subnotes to file"""
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
    return "".join(lines)


def get_note_index(lines, note):
    """Returns index note index if found, else -1"""
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


def format_note(note, subnotes_string):
    """Takes a note and formatted subnote string and returns formatted note"""
    return f"# {note}\n" + subnotes_string
