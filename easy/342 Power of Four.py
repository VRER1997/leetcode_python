class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ret = 1
        while ret <= num:
            if ret == num: return True
            ret *= 4
        return False