from pathlib import Path

import note_assistant


def test_default_filename_and_path():
    home_path = Path.home()
    test_file_path = Path(f"{home_path}/note_assistant/na.md")
    note_assistant.note_assistant("My random thought")

    assert test_file_path.is_file()
