# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        Sum = 0

        def helper(node):
            nonlocal Sum
            if not node:
                return False

            Sum += node.val

            if not node.left and not node.right and targetSum == Sum :
                return True

            if helper(node.right) or helper(node.left):
                return True
            
            Sum -= node.val
            return False
        
        return helper(root)