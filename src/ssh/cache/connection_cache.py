from typing import List
from pathlib import Path
from util import file
from dto.ConnectionInfoDto import ConnectionInfoDto
import json


CACHE_FILE = "connection-cache.json"
CACHE_FILE_FULL_PATH = f"{file.get_file_saving_dir()}/{CACHE_FILE}"


def _create() -> None:
    file_path = Path(CACHE_FILE_FULL_PATH)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text("")


def load() -> List[ConnectionInfoDto]:
    if file.is_file_available(CACHE_FILE_FULL_PATH):
        with open(CACHE_FILE_FULL_PATH, "r") as f:

            return [
                ConnectionInfoDto(**data) for data in json.loads(f.read())
            ]
    else:
        _create()

    return []


def destroy() -> None:
    file.delete_file(CACHE_FILE_FULL_PATH)


def add_entry(dto: ConnectionInfoDto) -> None:
    with open(CACHE_FILE_FULL_PATH, "r") as f:
        cache = json.load(f)
        cache.update(dto)


def remove_entry(dto: ConnectionInfoDto) -> None:
    with open(CACHE_FILE_FULL_PATH, "r") as f:
        cache = json.load(f)
        cache.remove(dto)
