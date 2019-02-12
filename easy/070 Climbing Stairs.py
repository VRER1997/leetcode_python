class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        list = [1,1]
        if n == 1: return 1
        for i in range(n-1):
            list.append(list[-1] + list[-2])
        return list[-1]