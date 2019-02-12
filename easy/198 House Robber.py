class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]
        n = len(nums)
        if n == 0: return 0
        dp.append(nums[0])
        if n == 1: return dp[-1]
        for i in range(1, n):
            t = max(dp[-1], nums[i] + dp[-2])
            dp.append(t)
        return dp[n]