#!/usr/bin/env python3

from argparse import ArgumentParser, Namespace
from collections import Counter
from itertools import permutations
from pathlib import Path

from .enums import Kind, Source
from .exceptions import BadMatchError


class Kouriae:
    def __init__(self) -> None:
        self.args: Namespace = self._parse_args()
        self.source: Source = self._check_source()
        self.kind: Kind = self._check_kind()
        self.input: str = self._read_input()
        self.output: str = self._encode_decode()

    @staticmethod
    def _parse_args() -> Namespace:
        parser = ArgumentParser()

        parser.add_argument(
            "-f",
            "--file",
            type=str,
            default=None,
            required=False,
            help="File with the text to encode/decode",
        )
        parser.add_argument(
            "-d",
            "--decode",
            type=bool,
            default=False,
            required=False,
            help="Decode the text",
        )

        return parser.parse_args()

    def _check_source(self) -> Source:
        match self.args.file:
            case None:
                return Source.STDIN

            case _:
                return Source.FILE

    def _check_kind(self) -> Kind:
        match self.args.decode:
            case False:
                return Kind.ENCODE

            case True:
                return Kind.DECODE

        raise BadMatchError(self.args.decode)

    def _read_input(self) -> str:
        match self.source:
            case Source.STDIN:
                return input()

            case Source.FILE:
                return Path(self.args.file).read_text()

        raise BadMatchError(self.kind)

    def _encode_decode(self) -> str:
        match self.kind:
            case Kind.ENCODE:
                return self._encode()

            case Kind.DECODE:
                return self._decode()

        raise BadMatchError(self.kind)

    def _encode(self) -> str:
        # k: u -> a, r: a -> u
        segments: tuple[str, ...] = ("ku", "ra", "ko", "re", "ki", "ri", "ke", "ro", "ka", "ru")

        words: list[str] = self.input.split()
        encoded_words: list[str] = words.copy()
        encode_key: str = ""
        seg_order: list = []
        last_seg: tuple[str] = ("",)
        perm_lv: int = 1
        idx: int = 0
        freq: dict[str, int] = {k: v for k, v in sorted(Counter(words).items(), key=lambda item: item[1], reverse=True)}

        for word in freq:
            if idx == len(tuple(permutations(segments, perm_lv))):
                perm_lv += 1
                idx = 0

            encoded_word: str = "".join(tuple(permutations(segments, perm_lv))[idx])
            encoded_words = [encoded_word if w == word else w for w in encoded_words]
            idx += 1

    def _decode(self) -> str:
        ...


def main() -> None:
    Kouriae()
