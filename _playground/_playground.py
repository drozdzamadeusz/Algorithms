import math

a = [1, 2]
b = [2, 1]

b.sort()

print(a == b)


def twoToPowOfN(n: int):
    if (n == 0):
        return 1
    res = 2 * twoToPowOfN(n - 1)
    print(f'Returning: {res}')
    return res


print(twoToPowOfN(4))

print(f'{1//2}')
