from note_assistant import note_assistant


def test_default_filename_and_path(tmp_path):
    note_assistant("My random thought", directory=tmp_path / "note_assistant/notes")

    path = tmp_path / "note_assistant/notes/na.md"
    assert path.exists()


def test_custom_filename_and_path(tmp_path):
    note_assistant("My random thought", directory=tmp_path, file_name="test")

    path = tmp_path / "test.md"
    assert path.exists()


def test_single_note_in_file(tmp_path):
    note_assistant("My random thought", directory=tmp_path)

    path = tmp_path / f"na.md"
    contents = path.read_text()
    assert contents == "My random thought\n"


def test_multiple_notes_in_file(tmp_path):
    note_assistant("My first thought", directory=tmp_path)
    note_assistant("My second thought", directory=tmp_path)
    note_assistant("My third thought", directory=tmp_path)

    path = tmp_path / f"na.md"
    contents = path.read_text()
    assert contents == "My first thought\nMy second thought\nMy third thought\n"
