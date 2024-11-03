from pathlib import Path

def main():
    home_path = Path.home()
    note_assistant_dir = Path(f"{home_path}/note_assistant")
    
    if not note_assistant_dir.is_dir():
        Path.mkdir(f"{home_path}/note_assistant")


if __name__ == "__main__":
    main()
