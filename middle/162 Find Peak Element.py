class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l <= r:
            if l == r: return l
            mid = l + ((r-l) >> 2)
            if nums[mid-1] < nums[mid]:
                l = mid+1
            else:
                r = mid-1