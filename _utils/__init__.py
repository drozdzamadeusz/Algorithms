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


def equal(output, expected=None, res_prefix="") -> bool:
    Text.printWithGap("")
    if not expected:
        print(Text.formatHeader(ResultType.INFO, res_prefix))
        Text.printWithGap(output)
        return True

    res = output == expected

    if res:
        print(Text.formatHeader(ResultType.PASSED, res_prefix))
    else:
        print(Text.formatHeader(ResultType.FAILED, res_prefix))
        Text.printWithGap(Text.color(Text.bold("Result: "), 'white'))
        Text.printWithGap(f'{output}\n')

    Text.printWithGap(Text.color(Text.bold("Expected: "), 'white'))
    Text.printWithGap(f'{expected}\n')

    return res


class Text:
    results = {
        ResultType.DEFAULT: lambda text, prefix = "": Text.color(Text.bold(prefix + text), 'white'),
        ResultType.PASSED: lambda text, prefix = "": Text.color(Text.bold(prefix + text if text else prefix + "✅ TEST PASSED"), 'green'),
        ResultType.FAILED: lambda text, prefix = "": Text.color(Text.bold(prefix + text if text else prefix + "❌ TEST FILED"), 'red'),
        ResultType.INFO: lambda text, prefix = "": Text.color(Text.bold(prefix + text if text else prefix + "ℹ️  RESULT:"), 'blue'),
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
    def printWithGap(text): return print("   " + f'{text}')


class Test:
    def __init__(self, numberOfTests) -> None:
        self.numberOfTests = numberOfTests
        self.counter = 0

    def getStatus(self):
        self.counter = +1
        return f'[{self.counter} / {self.numberOfTests}] '

    def equal(self, input, expected):
        return equal(input, expected, self.getStatus())
