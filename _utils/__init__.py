import time
from concurrent.futures import ProcessPoolExecutor, TimeoutError
from typing import Literal
from _utils.TextBuilder import BIG_GAP, DEF_GAP, Gaps, TextBuilder
from _utils.TextHeader import TextHeader
from _utils.helpers import formatArgs

TIMEOUT_SEC = 10000

UNSPECIFIED = "_UNSPECIFIED_"
TEST_HALTED_MSG = '\n⛔️ TESTING HALTED'
SUMMARY_MSG = '\n✓ Completed in {total_time:.2f} ms'
TESTS_NOT_RUN_MSG = '{not_run} {test_word} skipped after timeout!'
INDEX_MSG = '[{idx}/{total}] '
ELAPSED_MSG = ' {word} {elapsed:.{prec}f} ms'

TOutputMode = Literal['console_default', 'console_compact']
OUTPUT_MODE = 'console_default'

TTestMode = Literal['equal_result', 'execution_time']
TEST_MODE = 'equal_result'


class Test:
    def __init__(self,
                 fun=None,
                 timeout: int | Literal[False] = TIMEOUT_SEC,
                 mode: TTestMode = TEST_MODE,
                 output: TOutputMode = OUTPUT_MODE) -> None:
        self._fun = fun
        self._timeout = timeout
        self._mode = mode
        self._output_mode = output

        self._tests = []
        self._totalElapsed = 0

    def add(self, expect, *args, **kwargs) -> None:
        self._tests.append((expect, args, kwargs))

    def run(self) -> None:
        self.__print_header()

        idx, self._totalElapsed = 0, 0
        for test in self._tests:
            test_result, elapsed, timeout = self.__execute_test(test, idx)

            self._totalElapsed += elapsed

            timeStr = ELAPSED_MSG.format(word="in", elapsed=elapsed, prec=2)
            indexStr = self.__getIndex(idx)
            self.__print_result(test_result, test, indexStr, timeStr, timeout)

            idx += 1

        self.__print_summary(self._totalElapsed)

    def __print_result(self,
                       result,
                       test: tuple,
                       headerPrefix="",
                       headerSuffix="",
                       timeout=False,
                       *args) -> bool:
        expect, args, _ = test

        passed = result == expect
        noExpect = expect == UNSPECIFIED
        performance = self._mode == 'execution_time'
        headerType = TextHeader.parseHeaderType(
            passed, noExpect, timeout, performance)

        argsStr = (formatArgs(args) or "None") if args else ""

        argsLine = TextBuilder("Args:   ", True, 'grey',
                               '', f'{argsStr}', BIG_GAP)
        resLine = TextBuilder("Result: ", True, 'grey',
                              '', f'{result}', BIG_GAP)
        expLine = TextBuilder("Expect: ", True, 'grey', '',
                              f'{expect if not noExpect else ""}', BIG_GAP)

        TextBuilder().printEOL()
        TextHeader(headerType, headerPrefix, headerSuffix).print()

        if self._mode in ['equal_result']:
            if self._output_mode in ['console_default'] and\
                    (not passed or noExpect) and args:
                argsLine.print()                            # "Args" line in console

            if not timeout:
                resLine.print()                             # "Result" line in console

            if (not passed or timeout) and not noExpect:
                expLine.print()                             # "Expect" line in console

        return passed or noExpect

    def __getIndex(self, idx: str) -> str:
        return INDEX_MSG.format(idx=idx + 1, total=len(self._tests))

    def __execute_test(self, test: tuple, idx: int) -> tuple:
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
        TextBuilder(summaryStr, True, 'white').print()

    def __print_header(self):
        TextBuilder('Launching test engine...', True, 'white').printEOL().print().printEOL().text(
            'Mode:   ').suffix(self._mode.capitalize()).print().text(
            'Output: ').suffix(self._output_mode.capitalize()).print()


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(nodes: list[int]) -> TreeNode:
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    index = 1
    while queue and index < len(nodes):
        node = queue.pop(0)
        if node:
            if index < len(nodes) and nodes[index] is not None:
                node.left = TreeNode(nodes[index])
            queue.append(node.left)
            index += 1
            if index < len(nodes) and nodes[index] is not None:
                node.right = TreeNode(nodes[index])
            queue.append(node.right)
            index += 1
    return root
