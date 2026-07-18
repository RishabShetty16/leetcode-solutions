from collections import defaultdict, deque
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        nodes = defaultdict(lambda: defaultdict(list))

        q = deque([(root, 0, 0)])      # (node, column, row)

        while q:

            node, col, row = q.popleft()

            nodes[col][row].append(node.val)

            if node.left:
                q.append((node.left, col - 1, row + 1))

            if node.right:
                q.append((node.right, col + 1, row + 1))

        ans = []

        for col in sorted(nodes):

            vertical = []

            for row in sorted(nodes[col]):
                vertical.extend(sorted(nodes[col][row]))

            ans.append(vertical)

        return ans