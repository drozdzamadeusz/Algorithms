import copy
from enum import Enum
from typing import Literal
from termcolor import colored


DEF_TIMEOUT = 5000

UNSPECIFIED = "_UNSPECIFIED_"
DEF_GAP = "   "
BIG_GAP = "         "
HUGE_GAP = "                 "


class Gaps(Enum):
    R_NORMAL = 10
    L_NORMAL = 11
    R_BIG = 20
    L_BIG = 21
    R_HUGE = 30
    L_HUGE = 31


def parseGap(gap: Gaps):
    vals = {
        'NORMAL': DEF_GAP,
        'BIG': BIG_GAP,
        'HUGE': HUGE_GAP
    }
    pos = gap.name[:1]
    value = vals[gap.name[2:]]
    return (pos, value)


Color = Literal["red", "green", "yellow", "blue", "white", "grey"]


class TextBuilder:
    def __init__(self, text="", bold=False, color: Color = None, prefix="", suffix=""):
        self._text = text
        self._bold = bold
        self._color = color
        self._prefix = prefix
        self._suffix = suffix
        self._leftGap = None
        self._rightGap = None

    def text(self, text: str):
        self._text = text
        return self

    def prefix(self, prefix: str):
        self._prefix = prefix
        return self

    def suffix(self, suffix: str):
        self._suffix = suffix
        return self

    def bold(self, bold=True):
        self._bold = bold
        return self

    def gap(self, gap: Gaps):
        pos, val = parseGap(gap)
        if pos == 'L':
            self._leftGap = val
        elif pos == 'R':
            self._rightGap = val
        return self

    def color(self, color: Color):
        self._color = color
        return self

    def build(self) -> str:
        text = self._text
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
