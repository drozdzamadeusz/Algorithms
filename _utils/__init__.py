import os
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, TimeoutError
from enum import Enum
from typing import Literal
from termcolor import colored

UNSPECIFIED = "_UNSPECIFIED_"
DEF_GAP = "   "
BIG_GAP = "         "
TIMEOUT_SEC = 5000

Color = Literal["red", "green", "yellow", "blue", "white", "grey"]


class HeaderType(Enum):
    DEFAULT = 0
    FAILED = 1
    PASSED = 2
    NO_EXPECTED = 3
    TIMEOUT = 3


def equal(result, expect=UNSPECIFIED, headerPrefix="", headerSuffix="", gap=DEF_GAP, *args) -> bool:
    noExp = expect == UNSPECIFIED
    passed = result == expect
    args = f'{args[1:]}'[1:-1] if len(args) > 1 else "None"
    if args[-1] == ',': args = args[:-1]

    argsLine = Text.color(Text.bold("Args:   "), 'grey') + f'{args}'
    resLine = Text.color(Text.bold("Result: "), 'grey') + f'{result}'
    expLine = Text.color(Text.bold("Expect: "), 'grey') + f'{expect}'

    headerType = HeaderType.FAILED
    if passed: headerType = HeaderType.PASSED
    if noExp: headerType = HeaderType.NO_EXPECTED

    Text.printEOL()  # New line
    Text.print(Text.header(headerType, headerPrefix, headerSuffix))  # Header

    if not passed and not noExp:
        Text.printWithGap(argsLine, gap)  # "Args" line

    Text.printWithGap(resLine, gap)  # "Result" line

    if not passed and not noExp:
        Text.printWithGap(expLine, gap)  # "Expect" line

    return passed or noExp


class Text:
    headers = {
        HeaderType.DEFAULT: lambda t, p="", s="": Text.bold(p + t + s),
        HeaderType.PASSED: lambda t, p="", s="": Text.color(Text.bold(p + t + s if t else p + "✅ TEST PASSED"), 'green') + s,
        HeaderType.FAILED: lambda t, p="", s="": Text.color(Text.bold(p + t + s if t else p + "❌ TEST FAILED"), 'red') + s,
        HeaderType.NO_EXPECTED: lambda t, p="", s="": Text.color(Text.bold(p + t + s if t else p + "ℹ️  EXPECTED UNKNOWN"), 'blue') + s,
        HeaderType.TIMEOUT: lambda t, p="", s="": Text.color(Text.bold(p + t + s if t else p + "🟡 TEST TIMEOUT"), 'yellow') + s,
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
    def __init__(self, fun=None, timeout=TIMEOUT_SEC) -> None:
        self._fun = fun
        self._timeout = timeout
        self.tests = []

    def __print_result(self, result, expect, headerPrefix, headerSuffix, *args) -> bool:
        return equal(result, expect, headerPrefix, headerSuffix, BIG_GAP, *args)

    def __getIndex(self, index) -> str:
        return f'[{index}/{len(self.tests)}] '

    def add(self, expect, *args, **kwargs) -> None:
        self.tests.append((expect, args, kwargs))

    def run(self) -> None:
        idx, totalTime = 0, 1
        for expect, args, kwargs in self.tests:
            headerPrefix = self.__getIndex(idx)
            start_time = time.time()

            with ProcessPoolExecutor(max_workers=1) as executor:
                future = executor.submit(self._fun, *args, **kwargs)
                try:
                    result = future.result(timeout=self._timeout / 1000)
                except TimeoutError:
                    Text.print(Text.header(
                        HeaderType.TIMEOUT, f'\n{headerPrefix}', f' after {self._timeout} ms'))
                    Text.print(Text.color(
                        Text.bold('\n⛔️ TESTING PROCESS HALTED'), 'red'))
                    notRun = len(self.tests) - idx
                    if notRun > 0:
                        Text.printWithGap(Text.color(Text.bold(
                            f'{notRun} {"test" if notRun == 1 else "tests"} not run!'), 'white'))
                    Text.print(Text.color(
                        Text.bold(f'\nℹ️  Finished in {(totalTime + self._timeout):.2f} ms'), 'grey'))
                    os._exit(1)

            testTime = (time.time() - start_time) * 1000
            totalTime += testTime
            self.__print_result(result, expect, headerPrefix,
                                f' in {testTime:.2f} ms', '', *args)
            idx += 1

        Text.print(Text.color(
            Text.bold(f'\nℹ️  Finished in {totalTime:.2f} ms'), 'blue'))
