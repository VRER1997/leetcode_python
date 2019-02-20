class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        dp = [False] * len(s)  # dp[i] 表示[0,..i]可以被划分
        cache = {}
        dp[0] = True if s[0] in wordDict else False
        for i in range(1, len(s)):
            for j in range(0,i+1):
                if j == 0:
                    dp[i] |= (s[j:i+1] in wordDict)
                else:
                    dp[i] |= (dp[j-1] & (s[j:i+1] in wordDict))
                print(i, j, dp)
        return dp[-1]
        # 记忆化搜索 beat 5%
        '''
        cache = {}
        def dfs(s):
            if s == None or s == '':
                return True
            if s in cache: return cache[s]
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    if dfs(s[i:]):
                        cache[s[i:]] = True
                        return True
                    else:
                        cache[s[i:]] = False
            return False
        return dfs(s)
        '''
if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("ab", ["a", "b"]))