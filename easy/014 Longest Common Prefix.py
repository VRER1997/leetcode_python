class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        res = strs[0]
        for i in range(len(strs)):
            res = self.getTwoWordCommomPrefix(res, strs[i])
        return res


    def getTwoWordCommomPrefix(self, x, y):
        res, i = '', 0
        while i < len(x) and i < len(y):
            if x[i] == y[i]:
                res += x[i]
            else:
                break
            i += 1
        return res

if __name__ == '__main__':
    s = Solution()
    s.getTwoWordCommomPrefix("fl", "fl")