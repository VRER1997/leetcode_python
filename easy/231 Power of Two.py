class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ret = 1
        while ret <= n:
            if ret == n: return True
            ret *= 2
        return False