from enum import Enum
from typing import Literal
from termcolor import colored


class ResultType(Enum):
    FAILED = 0
    PASSED = 1


Color = Literal[
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "white",
]


def equal(input, expected, res_prefix="") -> bool:
    result = input == expected
    if result:
        print(Text.formatHeader(ResultType.PASSED, res_prefix, ""))
        return True
    else:
        print(Text.formatHeader(ResultType.FAILED, res_prefix, ""))
        Text.printWithGap(Text.color(Text.bold("Value: "), 'blue'))
        Text.printWithGap(input)
        Text.printWithGap(Text.color(Text.bold("Expected: "), 'blue'))
        Text.printWithGap(expected)
        return False


class Text:
    results = {
        ResultType.PASSED: lambda text, prefix = "": Text.color(Text.bold(prefix + text if text else prefix + "✅ TEST PASSED"), 'green'),
        ResultType.FAILED: lambda text, prefix = "": Text.color(Text.bold(prefix + text if text else prefix + "❌ TEST FILED"), 'red'),
    }

    @staticmethod
    def bold(text):
        return '\033[1m' + text + '\033[0m'

    @staticmethod
    def color(text: object, color: Color):
        return colored(text, color)

    @staticmethod
    def formatHeader(type, prexif, text):
        return Text.results[type](text, prexif)

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
