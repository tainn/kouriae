from enum import Enum, auto


class Source(Enum):
    STDIN = auto()
    FILE = auto()


class Kind(Enum):
    ENCODE = auto()
    DECODE = auto()
