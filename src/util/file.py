from pathlib import Path
import os

USER_DIR: str = ".python-ssh-gui"
HOME_PATH = Path.home()

def get_file_saving_dir() -> str:
    return f"{HOME_PATH}/{USER_DIR}"

def is_file_available(full_path: str) -> bool:
    return os.path.exists(full_path) and os.path.isfile(full_path)

def delete_file(full_path: str) -> None:
    os.remove(full_path)
