from _utils import Test, equal

# Created using "Test" calss
print("\n\nAdded using \"Test\" calss:")

Test = Test()

Test.add(result=[1, 2, 3, 4], expect=[1, 2, 3, 4])
Test.add(result=[5, 6, 7, 8], expect=[2, 1, 3, 7])
Test.add(result=[7, 8, 9, 10])

Test.run()


# Method "equal" called directly
print("\n\nMethod \"equal\" called directly:")

equal(result=[1, 2, 3, 4], expect=[1, 2, 3, 4])
equal(result=[5, 6, 7, 8], expect=[2, 1, 3, 7])
equal(result=[7, 8, 9, 10])

