# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def hight(root):
            if not root:
                return 0
            
            left_hight = hight(root.left)
            right_hight = hight(root.right)

            if abs(left_hight - right_hight) > 1:
                balanced[0] = False
                return 0
            
            return 1 + max(left_hight, right_hight)
        
        hight(root)
        return balanced[0]