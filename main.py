from pathlib import Path

def main():
    path = Path.home() / "note_assistant"
    path.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    main()
