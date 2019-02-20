class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        nums.sort()
        return nums[0]
        """

        """
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        return nums[0]
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + ((r-l)>>2)
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] < nums[l]:
                r = mid - 1
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                return nums[l]