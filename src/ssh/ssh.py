import subprocess
import os


FILE_DIRECTORY: str = os.path.dirname(os.path.abspath(__file__))
SSH_COMMAND: str = "ssh.exp"


def connect(server: str, user: str, password: str) -> None:
    script_path = os.path.join(FILE_DIRECTORY, SSH_COMMAND)
    script_exec_command = f'expect "{script_path}" "{server}" "{user}" "{password}"'

    command = f"""
        if ! {script_exec_command}; then
            zenity --error --text='Error: Connecting to {user}@{server} failed.';
            exit 1; 
        fi;
        exec bash;
    """

    subprocess.Popen([
        "ptyxis", "-s", "--", "bash", "-c", command
    ])


