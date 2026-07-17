from typing import Optional, List

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        stack = [root]
        ans = []

        while stack:

            node = stack.pop()
            ans.append(node.val)

            # Push right first
            if node.right:
                stack.append(node.right)

            # Push left second
            if node.left:
                stack.append(node.left)

        return ans