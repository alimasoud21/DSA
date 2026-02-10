# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        n = 0
        def count(node):
            nonlocal n
            if not node:
                return 0
            node.left = count(node.left)
            node.right = count(node.right)
            n += 1
            return n
        return count(root)