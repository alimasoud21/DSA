"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, row, col):
            is_same = True
            for i in range(n):
                for j in range(n):
                    if grid[row][col] != grid[row + i][col + j]:
                        is_same = False
                        break
            if is_same:
                return Node(grid[row][col], True) # is leaf Node

            n = n // 2
            topLeft = dfs(n, row, col)
            topRight = dfs(n, row, col + n)
            bottomLeft = dfs(n, row + n, col)
            bottomRight = dfs(n, row + n, col + n)
            return Node(0, False,  topLeft, topRight, bottomLeft, bottomRight)

        return dfs(len(grid), 0, 0)