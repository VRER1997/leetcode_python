class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp1 = [nums[0]] * n # i表示[0..i]以i结尾的乘积最大连续子序列
        dp2 = [nums[0]] * n # i表示[0..i]以i结尾的乘积最小连续子序列
        for i in range(1, n):
            dp1[i] = max(nums[i], dp1[i-1]*nums[i], dp2[i-1]*nums[i])
            dp2[i] = min(nums[i], dp1[i-1]*nums[i], dp2[i-1]*nums[i])
        return max(dp1)