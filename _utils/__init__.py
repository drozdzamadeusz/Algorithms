import os
import time
from concurrent.futures import ProcessPoolExecutor, TimeoutError
from _utils.TextBuilder import BIG_GAP, DEF_GAP, Gaps, TextBuilder
from _utils.TextHeader import HeaderType, TextHeader
from _utils.helpers import formatArgs

TIMEOUT_SEC = 10000


UNSPECIFIED = "_UNSPECIFIED_"
TEST_HALTED_MSG = '\n⛔️ TESTING HALTED'
SUMMARY_MSG = '\nℹ️  Finished in {total_time:.2f} ms'
TESTS_NOT_RUN_MSG = '{not_run} {test_word} not run!'
INDEX_MSG = '[{idx}/{total}] '
ELAPSED_MSG = ' {word} {elapsed:.{prec}f} ms'


def equal(result=None, expect=UNSPECIFIED, headerPrefix="", headerSuffix="", gap=DEF_GAP, timeout=False, *args) -> bool:
    noExpect = expect == UNSPECIFIED
    passed = result == expect
    argsStr = formatArgs(args) or "None"
    headerType = TextHeader.parseHeaderType(passed, noExpect, timeout)

    argsLine = TextBuilder("Args:   ", True, 'grey', '', f'{argsStr}', gap)
    resLine = TextBuilder("Result: ", True, 'grey', '', f'{result}', gap)
    expLine = TextBuilder("Expect: ", True, 'grey', '',
                          f'{expect if not noExpect else ""}', gap)

    TextBuilder().printEOL()
    TextHeader(headerType, headerPrefix, headerSuffix).print()

    if not passed or noExpect:
        argsLine.print()            # "Args" line in console
    if not timeout:
        resLine.print()             # "Result" line in console
    if not passed and not noExpect:
        expLine.print()             # "Expect" line in console

    return passed or noExpect


class Test:
    def __init__(self, fun=None, timeout=TIMEOUT_SEC) -> None:
        self._fun = fun
        self._timeout = timeout
        self.tests = []

    def add(self, expect, *args, **kwargs) -> None:
        self.tests.append((expect, args, kwargs))

    def run(self) -> None:
        idx, totalElapsed = 0, 0
        for test in self.tests:
            _, test_result, test_time = self.__execute_test(test, idx)

            elapsed = (time.time() - test_time) * 1000
            totalElapsed += elapsed

            timeStr = ELAPSED_MSG.format(word="in", elapsed=elapsed, prec=2)
            prefix = self.__getIndex(idx)
            self.__print_result(test_result, test, prefix, timeStr)

            idx += 1

        self.__print_summary(totalElapsed)

    def __print_result(self, result: any, test: tuple, headerPrefix: str, headerSuffix: str, timeout=False) -> bool:
        expect, args, _ = test
        return equal(result, expect, headerPrefix, headerSuffix, BIG_GAP, timeout, args)

    def __getIndex(self, idx: str) -> str:
        return INDEX_MSG.format(idx=idx, total=len(self.tests))

    def __execute_test(self, test: tuple, idx: int) -> tuple:
        _, args, kwargs = test
        headerPref = self.__getIndex(idx)

        startTime = time.time()
        with ProcessPoolExecutor(max_workers=1) as executor:
            future = executor.submit(self._fun, *args, **kwargs)
            try:
                timeout = self._timeout / 1000 if self._timeout != 0 else None
                result = future.result(timeout=timeout)
                return (True, result, startTime)
            except TimeoutError:
                notRun = len(self.tests) - idx
                self.__handle_timeout(test, headerPref, notRun, startTime)
                return (False, None, startTime)

    def __handle_timeout(self, test: tuple, headerPref, notRun, startTime):
        timeStr = ELAPSED_MSG.format(
            word="after",
            elapsed=self._timeout,
            prec=0)
        self.__print_result(None, test, headerPref, timeStr, True)

        TextBuilder(TEST_HALTED_MSG, True, 'red').print()

        if notRun > 0:
            skippedStr = TESTS_NOT_RUN_MSG.format(
                not_run=notRun,
                test_word="test was" if notRun == 1 else "tests were")
            TextBuilder(skippedStr, True).gap(Gaps.L_NORMAL).print()

        totalTime = (time.time() - startTime) * 1000 + self._timeout
        self.__print_summary(totalTime)

        os._exit(1)  # Halt testing

    def __print_summary(self, totalTime):
        summaryStr = SUMMARY_MSG.format(total_time=totalTime)
        TextBuilder(summaryStr, True, 'blue').print()
