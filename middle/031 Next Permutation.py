class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        self.reverse(nums, i, n-1)
        if i > 0:
            for j in range(i, n):
                if nums[j] > nums[i - 1]:
                    self.swap(nums, i - 1, j)
                    break

    def reverse(self, nums, l, r):
        while l < r:
            self.swap(nums,l,r)
            l += 1
            r -= 1

    def swap(self, nums, l, r):
        nums[l], nums[r] = nums[r], nums[l]