class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return None
        Min_x = -2**63
        first, second, third = Min_x, Min_x, Min_x
        nums = set(nums)
        for num in nums:
            if num > first:
                second, third = first, second
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
        return first if len(nums) < 3 else third