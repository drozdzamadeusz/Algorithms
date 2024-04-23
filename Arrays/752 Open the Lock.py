from typing import Deque, List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        if target == '0000':
            return 0

        def move(d: str, right: bool):
            n = int(d) + (1 if right else -1)
            if n > 9:
                return '0'
            elif n < 0:
                return '9'
            return f'{n}'

        def options(pin: str, vis:set):
            opt = []
            for i in range(4):
                a = pin[:i] + move(pin[i], True) + pin[i + 1:]
                if int(a) != 0 and a not in vis:
                    opt.append(a)
            for i in range(4):
                b = pin[:i] + move(pin[i], False) + pin[i + 1:]
                if int(b) != 0 and b not in vis:
                    opt.append(b)
            return opt

        q = Deque(options('0000', set()))
        vis = set()
        steps = 0

        optStep = len(q)
            
        while q:
            steps += 1
            optNxtStep = 0
            for _ in range(optStep):

                curr = q.popleft()

                if curr in deadends or curr in vis:
                    continue
                
                if curr == target:
                    return steps
                
                
                vis.add(curr)
                nxtMoves = options(curr, vis)
                q.extend(nxtMoves)

                
                optNxtStep += len(nxtMoves)
            optStep = optNxtStep
        return -1

sol = Solution()
print(sol.openLock(
    deadends=["0201",
              "0101",
              "0102",
              "1212",
              "2002"],
    target="0202"))
# print(sol.openLock(
#     deadends=["10"],
#     target="11"))
