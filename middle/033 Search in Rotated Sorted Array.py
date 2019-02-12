class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]: l = mid+1
            else: r = mid

        pol = l
        ans = self.binary_search(target, nums[:pol])
        if ans == -1:
            ans = self.binary_search(target, nums[pol:])
            if ans != -1:
                ans += pol
        return ans

    def binary_search(self, target, nums):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < target: l = mid+1
            elif nums[mid] > target: r = mid-1
            else:
                return mid
        return -1