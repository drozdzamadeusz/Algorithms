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
