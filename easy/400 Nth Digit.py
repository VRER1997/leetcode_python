class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        now = 1
        while n > len(str(now)):
            n -= len(str(now))
            now += 1
        return int(str(now)[n-1])
