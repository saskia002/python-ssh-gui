from pathlib import Path

USER_DIR: str = ".python-ssh-gui"
HOME_PATH = Path.home()

def get_file_saving_dir() -> str:
    return f"{HOME_PATH}/{USER_DIR}"