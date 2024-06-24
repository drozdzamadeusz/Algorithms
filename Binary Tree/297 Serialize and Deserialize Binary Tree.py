from typing import Deque
from _utils import TreeNode


class Codec:

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""

        result = ""

        q = Deque([root])

        while q:
            curr = q.popleft()

            if curr == 'none':
                result += 'N;'
                continue

            result += f'{curr.val};'

            if curr.left:
                q.append(curr.left)
            else:
                q.append("none")

            if curr.right:
                q.append(curr.right)
            else:
                q.append("none")

        return result

    def deserialize(self, data: str) -> TreeNode:
        if data == "":
            return None

        data_array = Deque(data.split(';'))

        root_val = data_array.popleft()
        root = TreeNode(root_val)

        q = Deque([root])

        while q:
            curr = q.popleft()

            left_node_val = data_array.popleft()

            if left_node_val != 'N':
                left_node = TreeNode(left_node_val)
                q.append(left_node)
                curr.left = left_node

            right_node_val = data_array.popleft()

            if right_node_val != 'N':
                right_node = TreeNode(right_node_val)
                q.append(right_node)
                curr.right = right_node

        return root


t = TreeNode(
    val=1,
    left=TreeNode(
        val=2,
        left=TreeNode(4),
        right=TreeNode(
            val=5,
            left=TreeNode(9),
            right=TreeNode(10))
    ),
    right=TreeNode(
        val=3,
        left=TreeNode(6),
        right=TreeNode(7)
    )
)

t1 = TreeNode(
    val=1,
    left=TreeNode(2)
)

sol = Codec()
encoded = sol.serialize(t)
decoded = sol.deserialize(encoded)
