from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        if len(grid) == 0:
            return res
        n, m = len(grid), len(grid[0])
        dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if i == 0:
                        res += 1
                    if i == n-1:
                        res += 1
                    if j == 0:
                        res += 1
                    if j == m-1:
                        res += 1
                else:
                    for k in range(4):
                        temx, temy = i + dx[k], j + dy[k]
                        if temx < 0 or temx > n-1 or temy < 0 or temy > m-1: continue
                        if grid[temx][temy] == 1:
                            res += 1
        return res
        #print(res)


if __name__ == '__main__':
    s = Solution()
    grid = [[0,1,0,0],
             [1,1,1,0],
             [0,1,0,0],
             [1,1,0,0]]
    s.islandPerimeter(grid)