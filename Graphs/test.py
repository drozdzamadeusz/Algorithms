from enum import Enum
from typing import Literal
from termcolor import colored


class ResultType(Enum):
    FAILED = 0
    PASSED = 1


Color = Literal[
    "black",
    "grey",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "light_grey",
    "dark_grey",
    "light_red",
    "light_green",
    "light_yellow",
    "light_blue",
    "light_magenta",
    "light_cyan",
    "white",
]


class Format:
    @staticmethod
    def bold(text):
        return '\033[1m' + text + '\033[0m'

    @staticmethod
    def color(text: object, color: Color):
        return colored(text, color)

    results = {
        ResultType.PASSED: lambda text, prefix = "": Format.color(Format.bold(prefix + text if text else prefix + "✅ TEST PASSED"), 'green'),
        ResultType.FAILED: lambda text, prefix = "": Format.color(Format.bold(prefix + text if text else prefix + "❌ TEST FILED"), 'red'),
    }

    @staticmethod
    def formatHeader(type, prexif, text):
        return Format.results[type](text, prexif)

    @staticmethod
    def printWithGap(text): return print("   " + f'{text}')


def equal(input, expected, res_prefix="") -> bool:
    result = input == expected
    if result:
        print(Format.formatHeader(ResultType.PASSED, res_prefix, ""))
        return True
    else:
        print(Format.formatHeader(ResultType.FAILED, res_prefix, ""))
        Format.printWithGap(Format.color(Format.bold("Value: "), 'blue'))
        Format.printWithGap(input)
        Format.printWithGap(Format.color(Format.bold("Expected: "), 'blue'))
        Format.printWithGap(expected)
        return False


class Test:
    def __init__(self, numberOfTests) -> None:
        self.numberOfTests = numberOfTests
        self.counter = 0

    def getStatus(self):
        self.counter = +1
        return f'[{self.counter} / {self.numberOfTests}] '

    def equal(self, input, expected):
        return equal(input, expected, self.getStatus())
