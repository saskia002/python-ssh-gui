from dataclasses import dataclass


@dataclass
class ConnectionInfoDto:
    server: str
    user: str
    password: str