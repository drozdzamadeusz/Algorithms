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

TOutputMode = Literal['console_default', 'console_compact']
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

            idxStr = self.__indexFormat(i)
            elapsedStr = self.__elapsedFormat(elapsed, timeoutHalt)
            self.__print_result(result, test, idxStr, elapsedStr, timeoutHalt)

        self.__print_summary(totalElapsed)

    def __print_result(self, result, test: TTest, prefix, suffix, timeout) -> bool:
        expect, args, _ = test
        passed = result == expect
        noExpect = expect == UNSPECIFIED

        headerType = self.__headerType(passed, noExpect, timeout)
        argsStr = (self.__formatArgs(args) or "None") if args else ""

        builder = TextBuilder('', True, 'grey').gap(Gaps.L_BIG)
        argsLine = builder.copy().text("Args:   ").suffix(f'{argsStr}')
        resLine = builder.copy().text("Result: ").suffix(f'{result}')
        expLine = builder.copy().text("Expect: ").suffix(f'{expect}')

        TextHeader(headerType, prefix, suffix).textBuilder().printEOL().print()

        # Do not display additional info if other mode is selected
        if self._mode in ['equal_result']:
            if (self._output_mode in ['console_default']
                    and args and (not passed or noExpect)):
                argsLine.print()                                # "Args" line in console

            if not timeout:
                resLine.print()                                 # "Result" line in console

            if not noExpect and (not passed or timeout):
                expLine.print()                                 # "Expect" line in console

        return passed or noExpect

    def __indexFormat(self, idx: str) -> str:
        return INDEX_MSG.format(idx=idx + 1, total=len(self._tests))

    def __elapsedFormat(self, elapsed: float, timeoutHalt: bool) -> str:
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
        TextBuilder(summaryStr, True, 'white').printEOL().print()

    def __print_header(self):
        TextBuilder('Launching test engine...', True, 'white').printEOL().print().printEOL().text(
            'Mode:    ').suffix(self._mode.capitalize()).print().text(
            'Output:  ').suffix(self._output_mode.capitalize()).print().text(
            'Timeout: ').suffix(f'{self._timeout} ms').print()

    def __formatArgs(self, args: tuple):
        res = f'{args}'[2:-3]
        if res[-1] == ',':
            res = res[:-1]
        return res

    def __headerType(self, passed: bool, noExpect: bool, timeout: bool):
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
