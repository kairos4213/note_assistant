from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown


def display_output(note_path: Path) -> None:
    """Takes file path for note and prints pretty output to display"""

    console = Console()
    console.print(f"[bold]Saved to: [italic]{note_path}")

    with note_path.open("r") as file:
        content = file.read()
        md = Markdown(content)
        console.print(md)
