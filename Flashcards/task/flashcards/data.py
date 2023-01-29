from dataclasses import dataclass
from typing import List


@dataclass
class Card:
    term: str
    definition: str
    mistakes: int = 0


@dataclass
class HardestInfo:
    terms: List[str]
    mistakes: int
