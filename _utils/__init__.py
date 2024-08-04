from ast import FunctionType
import time
from concurrent.futures import ProcessPoolExecutor, TimeoutError
from typing import Any, Callable, Literal
from _utils.TextBuilder import BIG_GAP, Gaps, TextBuilder
from _utils.TextHeader import HeaderType, TextHeader

TIMEOUT_SEC = 10000

UNSPECIFIED = "_UNSPECIFIED_"
TEST_HALTED_MSG = '⛔️ TESTING HALTED'
SUMMARY_MSG = '✓ Completed in {total_time:.2f} ms'
TESTS_NOT_RUN_MSG = '{not_run} {test_word} skipped after timeout!'
INDEX_MSG = '[{idx}/{total}] '
ELAPSED_MSG = ' {word} {elapsed:.{prec}f} ms'

TOutputMode = Literal['console_default', 'console_compact', 'console_minimal']
OUTPUT_MODE_DEFAULT = 'console_default'

TTestMode = Literal['equal_result', 'execution_time']
TEST_MODE_DEFAULT = 'equal_result'

TTest = tuple[Any, tuple, dict[str, Any]]


class Test:
    def __init__(self,
                 fun: Callable,
                 timeout: int | Literal[False] = TIMEOUT_SEC,
                 mode: TTestMode = TEST_MODE_DEFAULT,
                 output: TOutputMode = OUTPUT_MODE_DEFAULT):
        self._fun = fun
        self._timeout = timeout
        self._mode = mode
        self._output_mode = output

        self._tests = []

    def add(self, expect, *args, **kwargs):
        self._tests.append((expect, args, kwargs))

    def run(self):
        self.__print_header()

        totalElapsed = 0
        for i, test in enumerate(self._tests):
            result, elapsed, timeoutHalt = self.__execute_test(test)
            totalElapsed += elapsed

            idxStr = self.__formatIndex(i)
            elapsedStr = self.__formatElapsed(elapsed, timeoutHalt)
            self.__print_result(result, test, idxStr, elapsedStr, timeoutHalt)

        self.__print_summary(totalElapsed)

    def __print_result(self, result, test: TTest, prefix, suffix, timeout):
        expect, args, _ = test
        passed = result == expect
        noExpect = expect == UNSPECIFIED

        headerType = self.__getHeaderType(passed, noExpect, timeout)
        TextHeader(headerType, prefix, suffix).getBuilder().printEOL().print()

        # Display additional info only if mode is set to equal_result
        if self._mode not in ['equal_result']:
            return

        builder = TextBuilder("", True, 'grey').gap(Gaps.L_BIG)

        if not timeout:
            builder.suffix(f'{result}').print("Result: ")

        if not noExpect and (not passed or timeout):
            builder.suffix(f'{expect}').print('Expect: ')

        if (self._output_mode in ['console_default', 'console_compact']
           and args and (not passed or noExpect)):
            builder.suffix(self.__formatArgs(args)).print("  Args: ")

    def __formatIndex(self, idx: str) -> str:
        return INDEX_MSG.format(idx=idx + 1, total=len(self._tests))

    def __formatElapsed(self, elapsed: float, timeoutHalt: bool) -> str:
        word = "after" if timeoutHalt else "in"
        return ELAPSED_MSG.format(word=word, elapsed=elapsed, prec=2)

    def __execute_test(self, test: TTest) -> tuple[Any, float, bool]:
        _, args, kwargs = test

        with ProcessPoolExecutor(max_workers=1) as executor:
            future = executor.submit(self._fun, *args, **kwargs)
            timeout = self._timeout / 1000 if self._timeout > 0 else None

            result = None
            timeoutStop = False
            startTime = time.time()
            try:
                result = future.result(timeout)
            except TimeoutError:
                timeoutStop = True
            finally:
                elapsed = (time.time() - startTime) * 1000
                return (result, elapsed, timeoutStop)

    def __print_summary(self, totalTime):
        summaryStr = SUMMARY_MSG.format(total_time=totalTime)
        TextBuilder(summaryStr, True, 'white').printEOL().print().printEOL()

    def __print_header(self):
        TextBuilder('Launching test engine...', True, 'white').printEOL().print().printEOL(
        ).text('Mode:    ').suffix(self._mode.capitalize()).print(
        ).text('Output:  ').suffix(self._output_mode.capitalize()).print(
        ).text('Timeout: ').suffix(f'{self._timeout} ms').print()

    def __formatArgs(self, args: tuple):
        if not args:
            return ""

        if self._output_mode in ['console_compact']:
            return f'{args}'[1:-1]

        result = ''
        builder_value = TextBuilder("").suffix('\n')
        builder_index = TextBuilder('', True, 'grey')
        for i, arg in enumerate(args):
            builder_value.text(f'{arg}')
            builder_value.color('white' if i % 2 == 0 else 'light_cyan')

            if i + 1 == len(args):
                builder_value.suffix("")

            builder_index.text(f'{i + 1}: ')

            if i == 1:
                builder_index.prefix('                 ')

            result += builder_index.build() + builder_value.build()

        return result

    def __getHeaderType(self, passed: bool, noExpect: bool, timeout: bool):
        performance = self._mode == 'execution_time'
        if timeout:
            return HeaderType.TIMEOUT
        if performance:
            return HeaderType.PERFORMANCE
        if noExpect:
            return HeaderType.NO_EXPECTED
        if passed:
            return HeaderType.PASSED
        return HeaderType.FAILED
