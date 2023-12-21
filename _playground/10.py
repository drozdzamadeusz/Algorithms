

from typing import Deque

isH = lambda i, k: not i % k
isT = lambda i, k: i % k == k - 1
isS = lambda i, k: i == k - 1

k = 2

# print(isH(0, k))
# print(isH(1, k))
# print(isH(2, k))
# print(isH(3, k))
# print(isH(4, k))
# print(isH(5, k))
# print(isH(6, k))
# print(isH(7, k))

# print()

# print(isT(0, k))
# print(isT(1, k))
# print(isT(2, k))
# print(isT(3, k))
# print(isT(4, k))
# print(isT(5, k))
# print(isT(6, k))
# print(isT(7, k))


i = 1

# Store head
if isH(i, k):
    print("isH")

elif isS(i, k):
    print("isS")

elif isT(i, k):
    print("isT")
