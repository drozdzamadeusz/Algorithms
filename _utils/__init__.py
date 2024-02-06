import os
import time
from concurrent.futures import ProcessPoolExecutor, TimeoutError
from typing import Literal
from _utils.TextBuilder import Gaps, TextBuilder
from _utils.TextHeader import HeaderType, TextHeader

UNSPECIFIED = "_UNSPECIFIED_"
TIMEOUT_SEC = 5000
DEF_GAP = "   "
BIG_GAP = "         "
Color = Literal["red", "green", "yellow", "blue", "white", "grey"]

clearArgs = lambda args: (
    str(args[1:])[1:-1].rstrip(',') if args[1:] else "None")


def equal(result, expect=UNSPECIFIED, headerPrefix="", headerSuffix="", gap=DEF_GAP, *args) -> bool:
    noExpect = expect == UNSPECIFIED
    passed = result == expect
    argsStr = clearArgs(args)
    headerType = TextHeader.parseHeaderType(passed, noExpect)

    argsLine = TextBuilder("Args:   ", True, 'grey', '', f'{argsStr}', BIG_GAP)
    resLine = TextBuilder("Result: ", True, 'grey', '', f'{result}', BIG_GAP)
    expLine = TextBuilder("Expect: ", True, 'grey', ''
                          f'{expect if not noExpect else ""}', BIG_GAP)

    TextBuilder().printEOL()
    TextHeader(headerType, headerPrefix, headerSuffix).print()

    if not passed or noExpect:
        argsLine.print()            # "Args" line in console
    resLine.print()                 # "Result" line in console
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

    def __print_result(self, result, expect, headerPrefix, headerSuffix, *args) -> bool:
        return equal(result, expect, headerPrefix, headerSuffix, BIG_GAP, *args)

    def __getIndex(self, index) -> str:
        return f'[{index}/{len(self.tests)}] '

    def __execute_test(self, test, idx) -> tuple:
        _, args, kwargs = test
        headerPrefix = self.__getIndex(idx)

        startTime = time.time()
        
        with ProcessPoolExecutor(max_workers=1) as executor:
            future = executor.submit(self._fun, *args, **kwargs)
            try:
                result = future.result(timeout=self._timeout / 1000)
                return (True, result, startTime)
            except TimeoutError:
                skiped = len(self.tests) - idx
                self.__handle_timeout(headerPrefix, skiped, startTime)
                return (False, None, startTime)

    def run(self) -> None:
        idx, totalTime = 0, 0
        for test in self.tests:
            result, test_result, start_time = self.__execute_test(test, idx)
            if not result:
                break  # Exit due to timeout
            testTime = (time.time() - start_time) * 1000
            totalTime += testTime
            elapsed = f' in {testTime:.2f} ms'
            pref = self.__getIndex(idx)
            self.__print_result(
                test_result, test[0], pref, elapsed, '', *test[1])
            idx += 1
        self.__print_summary(totalTime)

    def __handle_timeout(self, headerPrefix, notRun, start_time):
        TextHeader(HeaderType.TIMEOUT,
                   f'\n{headerPrefix}', f' after {self._timeout} ms').print()
        TextBuilder('\n⛔️ TESTING PROCESS HALTED', True, 'red').print()

        if notRun > 0:
            TextBuilder(
                f'{notRun} {"test" if notRun == 1 else "tests"} not run!', True).gap(Gaps.L_NORMAL).print()

        totalTime = (time.time() - start_time) * 1000 + self._timeout
        self.__print_summary(totalTime)
        os._exit(1)

    def __print_summary(self, totalTime):
        TextBuilder(
            f'\nℹ️  Finished in {totalTime:.2f} ms', True, 'blue').print()
