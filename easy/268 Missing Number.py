class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = len(nums)
        for index, num in enumerate(nums):
            sum ^= index
            sum ^= num
        return sum