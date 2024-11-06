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

    path = tmp_path / "na.md"
    contents = path.read_text()
    assert contents == "# My random thought\n"


def test_multiple_notes_in_file(tmp_path):
    note_assistant("My first thought", directory=tmp_path)
    note_assistant("My second thought", directory=tmp_path)
    note_assistant("My third thought", directory=tmp_path)

    path = tmp_path / "na.md"
    contents = path.read_text()
    assert contents == "# My first thought\n# My second thought\n# My third thought\n"


def test_note_with_single_tag(tmp_path):
    note_assistant("My random thought with a tag", directory=tmp_path, tags=["random"])

    path = tmp_path / "random/na.md"
    assert path.exists()


def test_note_with_multiple_tags(tmp_path):
    note_assistant(
        "My random thought with a tag",
        directory=tmp_path,
        tags=["random", "test", "deep_test"],
    )

    path = tmp_path / "random/test/deep_test/na.md"
    assert path.exists()


def test_note_with_subnote(tmp_path):
    note_assistant(
        "My random thought",
        directory=tmp_path,
        subnotes=["Subnote about my random note"],
    )

    path = tmp_path / "na.md"
    contents = path.read_text()
    assert contents == "# My random thought\n- Subnote about my random note\n"


def test_note_with_multi_subnotes(tmp_path):
    note_assistant(
        "My random thought",
        directory=tmp_path,
        subnotes=["Subnote about my random note", "Second subnote", "Third subnote"],
    )

    path = tmp_path / "na.md"
    contents = path.read_text()
    assert (
        contents
        == "# My random thought\n- Subnote about my random note\n- Second subnote\n- Third subnote\n"
    )
