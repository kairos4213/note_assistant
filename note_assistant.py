from pathlib import Path


def note_assistant(note, directory="notes", file_name="na"):
    path = Path.home() / "note_assistant" / Path(directory) / f"{file_name}.md"
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a") as file:
        file.write(f"{note}\n")
