import os
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, TimeoutError
from enum import Enum
from typing import Literal
from termcolor import colored

UNSPECIFIED = "_UNSPECIFIED_"
DEF_GAP = "   "
BIG_GAP = "         "
TIMEOUT = 2

Color = Literal["red", "green", "yellow", "blue", "white", "grey"]


class HeaderType(Enum):
    DEFAULT = 0
    FAILED = 1
    PASSED = 2
    NO_EXPECTED = 3
    TIMEOUT = 3


def equal(result, expect=UNSPECIFIED, headerPrefix="", headerSuffix="", gap=DEF_GAP) -> bool:
    noExp = expect == UNSPECIFIED
    passed = result == expect

    resLine = Text.color(Text.bold("Result: "), 'grey') + f'{result}'
    expLine = Text.color(Text.bold("Expect: "), 'grey') + f'{expect}'

    headerType = HeaderType.FAILED
    if passed: headerType = HeaderType.PASSED
    if noExp: headerType = HeaderType.NO_EXPECTED

    Text.printEOL()  # New line
    Text.print(Text.header(headerType, headerPrefix, headerSuffix))  # Header
    Text.printWithGap(resLine, gap)  # "Result" line

    if not passed and not noExp:
        Text.printWithGap(expLine, gap)  # "Expect" line

    return passed or noExp


class Text:
    headers = {
        HeaderType.DEFAULT: lambda t, p="", s="": Text.bold(p + t + s),
        HeaderType.PASSED: lambda t, p="", s="": Text.color(Text.bold(p + t + s if t else p + "✅ TEST PASSED" + s), 'green'),
        HeaderType.FAILED: lambda t, p="", s="": Text.color(Text.bold(p + t + s if t else p + "❌ TEST FAILED" + s), 'red'),
        HeaderType.NO_EXPECTED: lambda t, p="", s="": Text.color(Text.bold(p + t + s if t else p + "ℹ️  EXPECTED UNKNOWN" + s), 'blue'),
        HeaderType.TIMEOUT: lambda t, p="", s="": Text.color(Text.bold(p + t + s if t else p + "⚠️ TEST TIMEOUT" + s), 'yellow'),
    }

    @staticmethod
    def normal(text: str) -> str:
        return '\033[0m' + text + '\033[0m'

    @staticmethod
    def bold(text: str) -> str:
        return '\033[1m' + text + '\033[0m'

    @staticmethod
    def color(text: str, color: Color) -> str:
        return colored(text, color)

    @staticmethod
    def header(type: HeaderType, prefix="", sufix="", customText="") -> str:
        return Text.headers[type](customText, prefix, sufix)

    @staticmethod
    def printWithGap(text: str, gap=DEF_GAP) -> None:
        print(f'{gap}{text}', flush=True)

    @staticmethod
    def printEOL() -> None:
        print(flush=True)

    @staticmethod
    def print(text: str) -> None:
        print(text, flush=True)


class Test:
    def __init__(self, fun=None) -> None:
        self._fun = fun
        self.tests = []

    def __execute(self, result, expect, headerPrefix, headerSuffix) -> bool:
        return equal(result, expect, headerPrefix, headerSuffix, BIG_GAP)

    def __getIndex(self, index) -> str:
        return f'[{index}/{len(self.tests)}] '

    def equal(self, expect=UNSPECIFIED, *args, **kwargs) -> None:
        self.tests.append((expect, args, kwargs))

    def run(self) -> None:
        idx = 1
        for expect, args, kwargs in self.tests:
            headerPrefix = self.__getIndex(idx)
            start_time = time.time()

            with ProcessPoolExecutor(max_workers=1) as executor:
                future = executor.submit(self._fun, *args, **kwargs)
                try:
                    result = future.result(timeout=TIMEOUT)
                except TimeoutError:
                    Text.print(Text.header(HeaderType.TIMEOUT, f'\n{headerPrefix}', Text.normal(
                        Text.color(f' after {TIMEOUT} seconds', 'white'))))
                    os._exit(1)

            elapsedTime = (time.time() - start_time) * 1000
            self.__execute(result, expect, headerPrefix, Text.normal(
                Text.color(f' in {elapsedTime:.2f} ms', 'white')))

            idx += 1
