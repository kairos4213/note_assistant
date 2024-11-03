from pathlib import Path


def note_assistant(note, file_name="test"):
    path_home = Path.home()
    filename = file_name
    file_path = Path(f"{path_home}/note_assistant/{filename}.md")

    file_path.write_text(note)
