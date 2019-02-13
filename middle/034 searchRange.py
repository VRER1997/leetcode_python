class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or len(nums) == 0:
            return [-1,-1]
        l, r, ret = 0, len(nums)-1, []
        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
                ret.append(mid)
                break
            elif nums[mid] >= target: r = mid-1
            else: l = mid+1
        if not ret: return [-1,-1]

        r = len(nums)-1
        while l <= r:
            mid = l + ((r-l)>>2)
            if nums[mid] == target and (mid == len(nums)-1 or nums[mid+1] != target):
                ret.append(mid)
                break
            elif nums[mid] > target: r = mid-1
            else: l = mid+1
        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10], 8))