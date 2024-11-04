import note_assistant


def test_default_filename_and_path(tmp_path):
    t_dir = tmp_path / "tests"
    t_dir.mkdir(parents=True, exist_ok=True)
    t_filename = "na"

    note_assistant.note_assistant(
        "My random thought", directory=str(t_dir), file_name=t_filename
    )

    path = t_dir / "na.md"
    assert path.exists()


def test_custom_filename_and_path(tmp_path):
    t_dir = tmp_path / "tests"
    t_dir.mkdir(parents=True, exist_ok=True)
    t_filename = "test"

    note_assistant.note_assistant(
        "My random thought", directory=t_dir, file_name=t_filename
    )

    path = t_dir / "test.md"
    assert path.exists()


def test_single_note_in_file(tmp_path):
    t_dir = tmp_path / "tests"
    t_dir.mkdir(parents=True, exist_ok=True)
    t_filename = "na"

    note_assistant.note_assistant(
        "My random thought", directory=t_dir, file_name=t_filename
    )

    path = t_dir / f"{t_filename}.md"
    contents = path.read_text()
    assert contents == "My random thought\n"


def test_multiple_notes_in_file(tmp_path):
    t_dir = tmp_path / "tests"
    t_dir.mkdir()
    t_filename = "na"

    note_assistant.note_assistant(
        "My first thought", directory=t_dir, file_name=t_filename
    )
    note_assistant.note_assistant(
        "My second thought", directory=t_dir, file_name=t_filename
    )
    note_assistant.note_assistant(
        "My third thought", directory=t_dir, file_name=t_filename
    )

    path = t_dir / f"{t_filename}.md"
    contents = path.read_text()
    assert contents == "My first thought\nMy second thought\nMy third thought\n"
