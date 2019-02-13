class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #return factorial(m+n-2) / factorial(n-1) / factorial(m-1)
        dp = [1 for i in range(m)]
        for i in range(1,n):
            for j in range(1,m):
                dp[j] += dp[j-1]
        return dp[m-1]
