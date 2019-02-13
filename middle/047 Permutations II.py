class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0: return []
        if len(nums) == 1: return [nums]

        ret = []
        for i in range(len(nums)):
            pre = nums[i]
            rest = nums[:i] + nums[i+1:]
            for j in self.permuteUnique(rest):
                t = [pre] + j
                if t not in ret:
                    ret.append(t)

        return ret