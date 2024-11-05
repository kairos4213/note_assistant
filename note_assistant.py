from pathlib import Path


def note_assistant(note, directory="note_assistant/notes", file_name="na"):
    path = Path.home() / Path(directory) / f"{file_name}.md"
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a") as file:
        file.write(f"{note}\n")
