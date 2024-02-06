from enum import Enum
from _utils import TextBuilder


class HeaderType(Enum):
    DEFAULT = 'default'
    FAILED = 'failed'
    PASSED = 'passed'
    NO_EXPECTED = 'no_expected'
    TIMEOUT = 'timeout'


class TextHeader:
    _headers = {
        HeaderType.DEFAULT: lambda t, p="", s="": TextBuilder(p + t + s, True),
        HeaderType.PASSED: lambda t, p="", s="": TextBuilder(p + (t if t else "✅ TEST PASSED") + s, True, 'green'),
        HeaderType.FAILED: lambda t, p="", s="": TextBuilder(p + (t if t else "❌ TEST FAILED") + s, True, 'red'),
        HeaderType.NO_EXPECTED: lambda t, p="", s="": TextBuilder(p + (t if t else "ℹ️  EXPECTED UNKNOWN") + s, True, 'blue'),
        HeaderType.TIMEOUT: lambda t, p="", s="": TextBuilder(p + (t if t else "🟡 TEST TIMEOUT") + s, True, 'yellow'),
    }

    def __init__(self, type: HeaderType, prefix="", sufix="", customText=""):
        self.set(type, prefix, sufix, customText)

    def set(self, type: HeaderType, prefix="", sufix="", customText=""):
        self._header = self._headers[type](customText, prefix, sufix)

    def get(self):
        return self._header

    def build(self):
        return self._header.build()

    def print(self):
        return TextBuilder(self.build()).print()

    @staticmethod
    def parseHeaderType(passed: bool, noExpect: bool):
        header = HeaderType.FAILED
        if passed:
            header = HeaderType.PASSED
        if noExpect:
            header = HeaderType.NO_EXPECTED
        return header
