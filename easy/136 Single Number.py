class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 1
        for num in nums:
            res ^= num
        return res
    