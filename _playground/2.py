class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = TreeNode(1)


stack = []
stack1 = [node]
stack1 = [node, node]



print(f'{stack == True}')
print(f'{stack1 == True}')

print(f'{len(stack) == True}')

print(f'{len(stack1) == True}')

print(f'{1 == True}')
