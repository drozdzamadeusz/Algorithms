from enum import Enum
from _utils import TextBuilder


class HeaderType(Enum):
    DEFAULT = 'default'
    FAILED = 'failed'
    PASSED = 'passed'
    NO_EXPECTED = 'no_expected'
    TIMEOUT = 'timeout'


class TextHeader:
    def __init__(self, headerType: HeaderType, prefix="", suffix="", customText=""):
        self._headerType = headerType
        self._prefix = prefix
        self._suffix = suffix
        self._customText = customText
        self._header = self.buildHeader()

    def buildHeader(self):
        defaultMessages = {
            HeaderType.DEFAULT: ("", None),
            HeaderType.PASSED: ("✅ TEST PASSED", 'green'),
            HeaderType.FAILED: ("❌ TEST FAILED", 'red'),
            HeaderType.NO_EXPECTED: ("ℹ️  EXPECTED UNKNOWN", 'blue'),
            HeaderType.TIMEOUT: ("🟡 TEST TIMEOUT", 'yellow'),
        }

        text, color = defaultMessages.get(self._headerType, ("", None))
        text = self._customText if self._customText else text
        return TextBuilder(self._prefix + text, True, color).suffix(self._suffix)

    def get(self) -> TextBuilder:
        return self._header

    def build(self) -> str:
        return self.get().build()

    def print(self) -> None:
        print(self.build())

    @staticmethod
    def parseHeaderType(passed: bool, noExpect: bool, timeout: bool):
        if timeout:
            return HeaderType.TIMEOUT
        elif noExpect:
            return HeaderType.NO_EXPECTED
        elif passed:
            return HeaderType.PASSED
        else:
            return HeaderType.FAILED
