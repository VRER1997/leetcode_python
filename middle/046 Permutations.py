class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        '''
        def dfs(dct, cnt, r):
            if cnt == len(nums):
                ret.append(r[:])
                return
            for i in range(len(nums)):
                if i not in dct or dct[i] == 0:
                    dct[i] = 1
                    r.append(nums[i])
                    dfs(dct, cnt+1, r)
                    dct[i] = 0
                    r.pop()

        ret = []
        nums.sort()
        dfs({}, 0, [])
        return ret
        '''

        if len(nums) == 0: return []
        if len(nums) == 1: return [nums]
        res = []
        for i in range(len(nums)):
            prefix = nums[i]
            rest = nums[:i] + nums[i + 1:]
            for j in self.permute(rest):
                res.append([prefix] + j)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))
