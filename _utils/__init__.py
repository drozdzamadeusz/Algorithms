from enum import Enum
from typing import Literal
from termcolor import colored


class ResultType(Enum):
    DEFAULT = 0
    FAILED = 1
    PASSED = 2
    INFO = 3


Color = Literal[
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "white",
]


def equal(result, expected=None, header_prefix="", gap="   ") -> bool:
    Text.printWithGap("")

    if not expected:
        print(Text.formatHeader(ResultType.INFO, header_prefix))
        Text.printWithGap(Text.color(Text.bold("Result: "), 'blue'), gap)
        Text.printWithGap(result, gap)
        # Text.printWithGap(Text.color(Text.bold("\nNo Expected data"), 'white'), gap)
        return True

    res = result == expected

    if res:
        print(Text.formatHeader(ResultType.PASSED, header_prefix))
        Text.printWithGap(Text.color(Text.bold("Result: "), 'green'), gap)
        Text.printWithGap(expected, gap)
    else:
        print(Text.formatHeader(ResultType.FAILED, header_prefix))
        Text.printWithGap(Text.color(Text.bold("Result: "), 'red'), gap)
        Text.printWithGap(f'{result}\n', gap)
        Text.printWithGap(Text.color(Text.bold("Expected: "), 'red'), gap)
        Text.printWithGap(expected, gap)

    return res


class Text:
    results = {
        ResultType.DEFAULT: lambda text, prefix = "": Text.color(Text.bold(prefix + text), 'white'),
        ResultType.PASSED: lambda text, prefix = "": Text.color(Text.bold(prefix + text if text else prefix + "✅ TEST PASSED"), 'green'),
        ResultType.FAILED: lambda text, prefix = "": Text.color(Text.bold(prefix + text if text else prefix + "❌ TEST FILED"), 'red'),
        ResultType.INFO: lambda text, prefix = "": Text.color(Text.bold(prefix + text if text else prefix + "ℹ️  NO EXPECTED RESULT"), 'blue'),
    }

    @staticmethod
    def bold(text):
        return '\033[1m' + text + '\033[0m'

    @staticmethod
    def color(text: object, color: Color):
        return colored(text, color)

    @staticmethod
    def formatHeader(type, prefix, text=""):
        return Text.results[type](text, prefix)

    @staticmethod
    def printWithGap(text, gap="   "): return print(f'{gap}{text}')


class Test:
    def __init__(self) -> None:
        self.tests = []

    def equal(self, result, expected=None, res_prefix="") -> bool:
        GAP = '         '
        return equal(result, expected, res_prefix, GAP)

    def getIndex(self, index):
        return f'[{index}/{len(self.tests)}] '

    def add(self, result, expected=None):
        obj = {"result": result, "expected": expected}
        self.tests.append(obj)

    def run(self):
        for idx, test in enumerate(self.tests):
            result = test['result']
            expacted = test['expected'] if 'expected' in test else None
            self.equal(result, expacted, self.getIndex(idx + 1))
