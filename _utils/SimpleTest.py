from _utils import Test

Test = Test()
result = [[1, 2, 3, 4], [5, 6, 7, 8]]
expected = [[1, 2, 3, 4], [5, 6, 7, 8]]
Test.add(result, expected)

result = [[1, 2, 3, 4]]
expected = [[5, 6, 7, 8]]
Test.add(result, expected)

result = [[1, 2, 3]]
Test.add(result)
Test.run()