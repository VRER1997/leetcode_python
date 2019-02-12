class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        res = float('inf')
        res_sum = []
        for i in range(n):
            left = i+1
            right = n-1
            while left < right:
                temp_sum = nums[i] + nums[left] + nums[right]
                abs_dict = abs(temp_sum - target)

                if abs_dict <= res:
                    res = abs_dict
                    res_sum.append(temp_sum)
                if temp_sum - target < 0:
                    left += 1
                if temp_sum - target > 0:
                    right -= 1
                if temp_sum == target:
                    return temp_sum
        return res_sum[-1]