from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        ans = []
        q = deque([root])
        leftToRight = True

        while q:

            size = len(q)
            level = [0] * size

            for i in range(size):

                node = q.popleft()

                if leftToRight:
                    index = i
                else:
                    index = size - 1 - i

                level[index] = node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(level)
            leftToRight = not leftToRight

        return ans