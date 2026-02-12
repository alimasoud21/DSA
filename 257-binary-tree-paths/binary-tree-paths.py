class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        res = []
        def paths(node, path):
            if node:
                path += str(node.val)

                if not node.left and not node.right:
                    res.append(path)
                else:
                    path += "->"
                    paths(node.left, path)
                    paths(node.right, path)

        paths(root, "")
        return res