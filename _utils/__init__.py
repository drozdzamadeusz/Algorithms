from enum import Enum
from typing import Literal
from termcolor import colored

UNSPECIFIED = "_UNSPECIFIED_"
DEF_GAP = "   "
BIG_GAP = "         "

Color = Literal["red", "green", "yellow", "blue", "white", "grey"]


class HeaderType(Enum):
    DEFAULT = 0
    FAILED = 1
    PASSED = 2
    NO_EXPECTED = 3


def equal(result, expect=UNSPECIFIED, headerPrefix="", gap=DEF_GAP) -> bool:
    noExp = expect == UNSPECIFIED
    passed = result == expect

    resLine = Text.color(Text.bold("Result: "), 'grey') + f'{result}'
    expLine = Text.color(Text.bold("Expect: "), 'grey') + f'{expect}'

    headerType = HeaderType.FAILED
    if passed: headerType = HeaderType.PASSED
    if noExp: headerType = HeaderType.NO_EXPECTED

    Text.printEOL()  # New line
    Text.print(Text.header(headerType, headerPrefix))  # Header
    Text.printWithGap(resLine, gap)  # "Result" line

    if not passed and not noExp:
        Text.printWithGap(expLine, gap)  # "Expect" line

    return passed or noExp


class Text:
    headers = {
        HeaderType.DEFAULT: lambda t, p = "": Text.bold(p + t),
        HeaderType.PASSED: lambda t, p = "": Text.color(Text.bold(p + t if t else p + "✅ TEST PASSED"), 'green'),
        HeaderType.FAILED: lambda t, p = "": Text.color(Text.bold(p + t if t else p + "❌ TEST FAILED"), 'red'),
        HeaderType.NO_EXPECTED: lambda t, p = "": Text.color(Text.bold(p + t if t else p + "ℹ️  EXPECTED UNKNOWN"), 'blue'),
    }

    @staticmethod
    def bold(text: str) -> str:
        return '\033[1m' + text + '\033[0m'

    @staticmethod
    def color(text: str, color: Color) -> str:
        return colored(text, color)

    @staticmethod
    def header(type: HeaderType, prefix="", customText="") -> str:
        return Text.headers[type](customText, prefix)

    @staticmethod
    def printWithGap(text: str, gap=DEF_GAP) -> None:
        return print(f'{gap}{text}')

    @staticmethod
    def printEOL() -> None:
        return print()

    @staticmethod
    def print(text: str) -> None:
        return print(text)


class Test:
    def __init__(self, fun = None) -> None:
        self.fun = fun
        self.tests = []

    def __execute(self, result, expect, headerPrefix) -> bool:
        return equal(result, expect, headerPrefix, BIG_GAP)

    def __getIndex(self, index) -> str:
        return f'[{index}/{len(self.tests)}] '

    def add(self, result, expect=UNSPECIFIED) -> None:
        obj = {"result": result, "expect": expect}
        self.tests.append(obj)

    def run(self) -> None:
        for idx, test in enumerate(self.tests):
            result = test['result']
            expact = test['expect']
            self.__execute(result, expact, self.__getIndex(idx + 1))
