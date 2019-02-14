class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        '''
        res = [[]]
        for n in nums:
            res += [item + [n] for item in res]
        return res
        '''

        '''
        n = len(nums)
        ret = [[]]
        for i in range(1,2 ** n):
            indexs = []
            s = str(bin(i))[2:][::-1]
            #print(i,s)
            for index, char in enumerate(s):
                if char == '1': indexs.append(nums[index])
            ret.append(indexs)
        return ret
        '''
        ret = []
        def dfs(cur, temp):
            if temp not in ret:
                ret.append(temp)
            if cur == len(nums): return
            dfs(cur+1, temp)
            dfs(cur+1, temp+[nums[cur]])
        dfs(0,[])
        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1,2,3]))