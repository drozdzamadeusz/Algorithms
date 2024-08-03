from enum import Enum
from _utils import TextBuilder


class HeaderType(Enum):
    DEFAULT = 'default'
    FAILED = 'failed'
    PASSED = 'passed'
    NO_EXPECTED = 'no_expected'
    TIMEOUT = 'timeout'
    PERFORMANCE = 'performance'


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
            HeaderType.PASSED: ("✅ PASSED", 'green'),
            HeaderType.FAILED: ("❌ FAILED", 'red'),
            HeaderType.NO_EXPECTED: ("ℹ️ EXPECTED RESULT UNKNOWN", 'blue'),
            HeaderType.TIMEOUT: ("⏰ TIMEOUT", 'yellow'),
            HeaderType.PERFORMANCE: ("✅ COMPLETED", 'green'),
        }

        text, color = defaultMessages.get(self._headerType, ("", None))
        text = self._customText if self._customText else text
        return TextBuilder(f'{self._prefix}{text}', True, color).suffix(self._suffix)

    def get(self) -> TextBuilder:
        return self._header

    def build(self) -> str:
        return self.get().build()

    def print(self) -> None:
        print(self.build())

    @staticmethod
    def parseHeaderType(passed: bool, noExpect: bool, timeout: bool, performance: bool):
        if timeout:
            return HeaderType.TIMEOUT
        if performance:
            return HeaderType.PERFORMANCE
        if noExpect:
            return HeaderType.NO_EXPECTED
        if passed:
            return HeaderType.PASSED
        return HeaderType.FAILED
