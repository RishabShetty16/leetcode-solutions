from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        ans = 0
        q = deque([(root, 0)])      # (node, index)

        while q:

            size = len(q)
            min_index = q[0][1]

            first = last = 0

            for i in range(size):

                node, index = q.popleft()

                # Normalize indices to avoid overflow
                index -= min_index

                if i == 0:
                    first = index

                if i == size - 1:
                    last = index

                if node.left:
                    q.append((node.left, 2 * index + 1))

                if node.right:
                    q.append((node.right, 2 * index + 2))

            ans = max(ans, last - first + 1)

        return ans