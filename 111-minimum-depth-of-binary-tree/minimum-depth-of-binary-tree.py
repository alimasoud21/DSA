# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        

        def helper(root):
            if not root:
                return 0

            left = helper(root.left)
            right = helper(root.right)

            if left == 0:
                return right + 1
            if right == 0:
                return left + 1

            return 1 + min(left, right)

        return helper(root)