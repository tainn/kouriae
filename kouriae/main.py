#!/usr/bin/env python3

import sys
from pathlib import Path

from .enums import Input
from .exceptions import NotAFileError, TooManyArgumentsError


class Kouriae:
    def __init__(self, args: list[str]) -> None:
        self.args: list[str] = args
        self.kind: Input = self._kind_check()

    def _kind_check(self) -> Input:
        if len(self.args) > 1:
            raise TooManyArgumentsError(f"{len(self.args)} provided, 1 allowed")

        if not self.args:
            return Input.STDIN

        if Path(self.args[0]).is_file():
            return Input.FILE

        raise NotAFileError(f"{self.args[0]} is not a file")


def main() -> None:
    kouriae = Kouriae(args=sys.argv[1:])
    print(kouriae.kind.name)
