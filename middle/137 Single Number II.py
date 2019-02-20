class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        a = b = 0
        for num in nums:
            b = b ^ num & ~a
            a = a ^ num & ~b
        return a | b

        """
        return (sum(set(nums))* 3 - sum(nums)) // 2
        """