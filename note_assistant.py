from pathlib import Path


def note_assistant(note, directory="note_assistant/notes", file_name="na", tags=None):
    if tags:
        tags_path = ""
        for tag in tags:
            tags_path += f"{tag}/"
        path = Path.home() / Path(directory) / f"{tags_path}{file_name}.md"
    else:
        path = Path.home() / Path(directory) / f"{file_name}.md"
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a") as file:
        file.write(f"# {note}\n")
