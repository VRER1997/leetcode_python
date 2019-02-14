class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        nums.sort()
        for i in range(1, pow(2,len(nums))):
            tem = []
            s = str(bin(i))[2:][::-1]
            for index, char in enumerate(s):
                if char == '1':
                    tem.append(nums[index])
            if tem not in ret:
                ret.append(tem)

        return ret
