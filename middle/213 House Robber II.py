from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        elif n == 1: return nums[0]
        elif n == 2: return max(nums[0], nums[1])

        dp = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            for j in range(i, n):
                if j == i:
                    dp[i][j] = nums[j]
                elif j == i+1:
                    dp[i][j] = max(nums[i], nums[i+1])
                else:
                    dp[i][j] = max(dp[i][j-2] + nums[j], dp[i][j-1])

        # rob without n-1, or rob with  n-1
        val = max(dp[0][n-2], dp[1][n-3] + nums[n-1])

        return val
