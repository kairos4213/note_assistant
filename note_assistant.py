from pathlib import Path


def note_assistant(note, file_name="na.md"):
    path_home = Path.home()
    filename = file_name
    file_path = Path(f"{path_home}/note_assistant/{filename}")

    file_path.write_text(note)
