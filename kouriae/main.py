#!/usr/bin/env python3

import base64
import zlib
from argparse import ArgumentParser, Namespace
from collections import Counter
from itertools import permutations

from .enums import Kind


class Kouriae:
    def __init__(self) -> None:
        # k: u -> a, r: a -> u
        self.segments: tuple[str, ...] = (
            "ku",
            "ra",
            "ko",
            "re",
            "ki",
            "ri",
            "ke",
            "ro",
            "ka",
            "ru",
        )
        self.idx: int = 0
        self.perm_lv: int = 1

        self.args: Namespace
        self.kind: Kind
        self.input: str
        self.output: str
        self.key: str

        self._parse_args()
        self._check_kind()
        self._read_input()
        self._encode_decode()
        self._output()

    def _parse_args(self) -> None:
        parser = ArgumentParser()

        parser.add_argument(
            "-e",
            "--encode",
            action="store_true",
            default=True,
            required=False,
            help="Encode the text",
        )
        parser.add_argument(
            "-d",
            "--decode",
            action="store_true",
            default=False,
            required=False,
            help="Decode the text",
        )

        self.args = parser.parse_args()

    def _check_kind(self) -> None:
        match self.args.decode:
            case False:
                self.kind = Kind.ENCODE

            case True:
                self.kind = Kind.DECODE

    def _read_input(self) -> None:
        match self.kind:
            case Kind.ENCODE:
                self.input = input("text: ")

            case Kind.DECODE:
                self.input = input("text: ")
                self.key = input("key: ")

    def _encode_decode(self) -> None:
        match self.kind:
            case Kind.ENCODE:
                self._encode()

            case Kind.DECODE:
                self._decode()

    def _encode(self) -> None:
        encode_words: list[str] = self.input.split()
        encode_key: str = ""

        freq: dict[str, int] = {
            k: v
            for k, v in sorted(
                Counter(encode_words).items(),
                key=lambda item: item[1],
                reverse=True,
            )
        }

        for word in freq:
            perm_seg: str = self._next_perm_seg()
            encode_words = [perm_seg if w == word else w for w in encode_words]
            encode_key += f"{word}^"

        zl = zlib.compress(encode_key.strip("^").encode())
        b64 = base64.b64encode(zl)

        self.output = " ".join(encode_words)
        self.key = b64.decode()

    def _decode(self) -> None:
        decode_words: list[str] = self.input.split()
        de_b64: bytes = base64.b64decode(self.key.encode())
        decode_key: str = zlib.decompress(de_b64).decode()

        words: list[str] = decode_key.split("^")

        for word in words:
            perm_seg: str = self._next_perm_seg()
            decode_words = [word if w == perm_seg else w for w in decode_words]

        self.output = " ".join(decode_words)

    def _next_perm_seg(self) -> str:
        if self.idx == len(tuple(permutations(self.segments, self.perm_lv))):
            self.idx = 0
            self.perm_lv += 1

        perm_seg: str = "".join(tuple(permutations(self.segments, self.perm_lv))[self.idx])
        self.idx += 1

        return perm_seg

    def _output(self) -> None:
        match self.kind:
            case Kind.ENCODE:
                print()
                print(self.output)
                print(self.key)

            case Kind.DECODE:
                print()
                print(self.output)


def main() -> None:
    Kouriae()
