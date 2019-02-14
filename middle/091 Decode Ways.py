class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if s[0] == '0': return 0
        if n == 1 : return 1
        dp = [0 for i in range(n)]
        dp[0]=1
        for i in range(1, n):
            first = dp[i-1]
            second = 0
            if  10 <= int(s[i-1:i+1]) <= 26:
                second = dp[i-2] if i >=2 else 1
            if s[i] == '0':
                if 10 <= int(s[i - 1:i + 1]) <= 26:
                    first = 0
                else:
                    return 0
            print(i, first, second)
            dp[i] = first + second
        return dp[-1]
if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings("101"))