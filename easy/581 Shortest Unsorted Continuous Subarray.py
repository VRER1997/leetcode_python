from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sort = sorted(nums)
        i, j = 0, len(nums_sort)-1
        while i < len(nums) and nums[i] == nums_sort[i]:
            i += 1
        while j > 0 and nums[j] == nums_sort[j]:
            j -= 1
        return max(0, j-i+1)

if __name__ == '__main__':
    s = Solution()
    print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))