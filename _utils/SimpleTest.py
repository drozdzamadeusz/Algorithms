from _utils import Test

def fun(a): return a

if __name__ == '__main__':
    print("\n\nAdded using \"Test\" calss:")

    test = Test(fun)

    test.equal([1, 2, 3, 4], [1, 2, 3, 4])
    test.equal([5, 6, 7, 8], [2, 1, 3, 7])
    test.equal([7, 8, 9, 10], [])

    test.run()