class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2: return n

        idx = 0
        while idx < len(nums)-2:
            if nums[idx] == nums[idx+1] == nums[idx+2]:
                nums.pop(idx)
            else: idx += 1
        return len(nums)