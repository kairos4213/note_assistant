from pathlib import Path

import note_assistant

home_path = Path.home()

def test_default_filename_and_path():
    test_file_path = Path(f"{home_path}/note_assistant/na.md")
    note_assistant.note_assistant("My random thought")

    assert test_file_path.is_file()

def test_custom_filename_and_path():
    test_file_path = Path(f"{home_path}/note_assistant/test.md")
    note_assistant.note_assistant("My random thought", file_name="test")

    assert test_file_path.is_file()
