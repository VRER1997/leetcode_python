class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum, ans = 0, 0
        for i in range(len(nums)):
            if nums[i] < 0:
                if sum > ans : ans = sum
                sum += nums[i]
                if  sum < 0: sum = 0
            else:
                sum += nums[i]
        if sum > ans: ans = sum
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))