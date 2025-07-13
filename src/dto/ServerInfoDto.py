from dataclasses import dataclass


@dataclass
class ServerInfoDto:
    server: str
    user: str
    password: str