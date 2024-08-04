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
        self._textBuilder = self.__buildTextBuilder()

    def __buildTextBuilder(self):
        defaultMessages = {
            HeaderType.DEFAULT: ("", None),
            HeaderType.PASSED: ("✅ PASSED", 'green'),
            HeaderType.FAILED: ("❌ FAILED", 'red'),
            HeaderType.NO_EXPECTED: ("ℹ️ EXPECTED RESULT UNKNOWN", 'blue'),
            HeaderType.TIMEOUT: ("⏰ HALTED", 'yellow'),
            HeaderType.PERFORMANCE: ("✅ FINISHED", 'green'),
        }

        text, color = defaultMessages.get(self._headerType, ("", None))
        text = self._customText if self._customText else text
        return TextBuilder(f'{self._prefix}{text}', True, color).suffix(self._suffix)

    def textBuilder(self) -> TextBuilder:
        return self._textBuilder

    def build(self) -> str:
        return self.textBuilder().build()

    def print(self):
        print(self.build())
        return self
