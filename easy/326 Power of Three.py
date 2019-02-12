class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ret = 1
        while ret <= n:
            if ret == n: return True
            ret *= 3
        return False