import copy
from enum import Enum
from typing import Literal
from termcolor import colored


DEF_TIMEOUT = 5000

UNSPECIFIED = "_UNSPECIFIED_"
DEF_GAP = "   "
BIG_GAP = "         "

Color = Literal["red", "green", "yellow", "blue", "white", "grey"]


class Gaps(Enum):
    R_NORMAL = 0
    R_BIG = 10
    L_NORMAL = 1
    L_BIG = 11


class TextBuilder:
    def __init__(self,
                 text="",
                 bold=False,
                 color: Color = None,
                 prefix: str = None,
                 suffix: str = None,
                 leftGap=None,
                 rightGap=None,
                 header=None):
        self._text = text
        self._bold = bold
        self._color = color
        self._prefix = prefix
        self._suffix = suffix
        self._leftGap = leftGap
        self._rightGap = rightGap
        self._header = header

    def header(self, header):
        self._header = header
        return self

    def text(self, text: str):
        self._text = text
        return self

    def prefix(self, prefix: str):
        self._prefix = prefix
        return self

    def suffix(self, suffix: str):
        self._suffix = suffix
        return self

    def bold(self):
        self._bold = True
        return self

    def gap(self, gap: Gaps):
        onLeft = gap.name[:1] == 'L'
        val = DEF_GAP if gap.value < 10 else BIG_GAP
        if onLeft:
            self._leftGap = val
        else:
            self._rightGap = val
        return self

    def color(self, color: Color):
        self._color = color
        return self

    def build(self) -> str:
        text = self._header if self._header else self._text
        if self._leftGap:
            text = f"{self._leftGap}{text}"
        if self._bold:
            text = f"\033[1m{text}\033[0m"
        if self._color:
            text = colored(text, self._color)
        if self._prefix:
            text = f"{self._prefix}{text}"
        if self._suffix:
            text = f"{text}{self._suffix}"
        if self._rightGap:
            text = f"{text}{self._rightGap}"
        return text

    def print(self, text: str = None):
        if text is not None:
            self._text = text
        print(self.build(), flush=True)
        return self

    def printEOL(self):
        print(flush=True)
        return self

    def copy(self):
        return copy.copy(self)
