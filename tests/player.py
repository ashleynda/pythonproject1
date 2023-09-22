from dataclasses import dataclass


@dataclass(frozen=True)
class Player:
    name: str
    sign: str
