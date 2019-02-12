"""
# Definition for a QuadTree node.
"""
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight



class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        self.constructTree(grid, len(grid), 0, 0)

    def constructTree(self, grid, N, x, y):
        if N == 1 or self.getAllEqual(grid, N, x, y):
            return Node(grid[x][y] == 1, True, None, None, None, None)
        tl = self.constructTree(grid, N/2, x, y)
        tr = self.constructTree(grid, N/2, x, y+N/2)
        bl = self.constructTree(grid, N/2, x+N/2, y)
        br = self.constructTree(grid, N/2, x+N/2, y+N/2)

        return Node((True if grid[x][y] else False), False,
                    tl, tr, bl, br)

    def getAllEqual(self, grid, N, x, y):
        w = grid[x][y]
        for i in range(x, x+N+1):
            for j in range(y, y+N+1):
                if grid[i][j] != w:
                    return False
        return True