class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in map:
                return [map[another_num], index]
            else:
                map[num] = index
        return None

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
