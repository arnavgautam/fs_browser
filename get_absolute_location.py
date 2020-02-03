from pathlib import Path
import sys

def resolve_path(path):
    home_dir = Path(path).expanduser().resolve()
    if not (home_dir.exists() and home_dir.is_dir()):
        raise ValueError
    return home_dir

if __name__ == "__main__":
    try:
        resolved_path = resolve_path(sys.argv[1])
        print(resolved_path)
    except Exception as e:
        raise e