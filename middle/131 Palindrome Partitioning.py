class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.ret = []
        isPalindrome = lambda s:  s == s[::-1]
        def dfs(s, path):
            if not s:
                self.ret.append(path)
                return
            for i in range(1,len(s)+1):
                if isPalindrome(s[:i]):
                    dfs(s[i:], path + [s[:i]])
        dfs(s,[])
        return self.ret