# Note Assistant

A minimal CLI tool for capturing notes, thoughts, and reminders directly from your terminal — without breaking your flow.

## Motivation

While working through [boot.dev](https://www.boot.dev) coursework, I kept losing track of notes and ideas. As a father of twins (now two sets of twins), context-switching is constant — I needed a way to jot something down fast, without reaching for another app or taking my eyes off the screen.

Note Assistant is the result: a single command that captures a thought and gets out of the way.

## Quick Start

**Requirements:** Python 3.12+, [uv](https://docs.astral.sh/uv/)

```bash
git clone https://github.com/kairos4213/note_assistant
cd note_assistant
uv sync
```

**Global install** — makes `na` available system-wide in any terminal session:

```bash
uv tool install .
```

**Editable install** — installs into the project venv, useful for development:

```bash
uv pip install -e .
```

Then capture your first note:

```bash
na "Remember to look up argparse and click"
```

## Usage

Notes are stored as markdown files under `~/note_assistant/notes/na.md` by default.

#### Basic note

```bash
na "My thought"
```

#### Custom directory and filename

```bash
na "My thought" -d "projects/my_project" -f "ideas"
```

Stores the note at `~/projects/my_project/ideas.md`.

#### Tags (subdirectories)

```bash
na "My thought" -d "projects/my_project" -t "backend" -t "auth"
```

Each tag becomes a nested subdirectory: `~/projects/my_project/backend/auth/na.md`.

#### Subnotes

```bash
na "Info dump" -s "Idea one" -s "Idea two" -s "Idea three"
```

Subnotes are stored as list items under the note header.

#### Appending to an existing note

Running the same note text again adds new subnotes without removing existing ones:

```bash
na "Info dump" -s "One more idea"
```

#### All options

| Flag | Long form | Description |
|---|---|---|
| | `note` | The note text (required) |
| `-d` | `--directory` | Storage directory relative to home (default: `note_assistant/notes`) |
| `-f` | `--filename` | Markdown filename without extension (default: `na`) |
| `-t` | `--tag` | Subdirectory tag, repeatable for nesting |
| `-s` | `--subnote` | Subnote item, repeatable |

## Contributing

Feedback, ideas, and contributions are welcome — this is a learning project that I built awhile ago and am now revisiting, I expect to make a few changes here and there, but this is not my main priority.

- Found a bug or have a feature idea? [Open an issue](https://github.com/kairos4213/note_assistant/issues)
- Want to contribute? Fork the repo, make your changes, and open a pull request
- All feedback is appreciated — just keep it kind
