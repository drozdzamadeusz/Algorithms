from typing import Deque


class Solution:
    def countOfAtoms(self, formula: str) -> str:

        table = {}

        factors = []
        last_num = 1  

        name = ''

        prev = ''
        for i in range(len(formula) - 1, -1, -1):
            c = formula[i]

            if c == ')':
                factors.append(last_num)
                last_num = 1

            elif c == '(':
                factors.pop()
                last_num = 1

            
            elif c.isdigit():
                if prev.isdigit():
                    last_num = int(f'{c}{last_num}')
                else:
                    last_num = int(c)


            elif ord('a') <= ord(c) <= ord('z'):
                name = c + name      

            elif ord('A') <= ord(c) <= ord('Z'):
                name = c + name

                curr = last_num
                for f in factors:
                    curr *= f

                table[name] = table.get(name, 0) + curr
                
                last_num = 1
                name = ''

            prev = c

        res = ''
        for k, v in sorted(table.items()):
            res += k
            if v != 1:
                res += f'{v}'

        return res



sol = Solution()
print(sol.countOfAtoms("Be32"))
