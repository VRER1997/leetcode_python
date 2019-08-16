from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        n, m = len(matrix), len(matrix[0])

        dp = []

        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(int(matrix[i][j]))
            dp.append(temp)

        for i in range(1, n):
            for j in range(1, m):
                if dp[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

        res = 0
        for i in range(n):
            for j in range(m):
                if dp[i][j] > res:
                    res = dp[i][j];

        return res