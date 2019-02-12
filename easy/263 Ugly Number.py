class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        for x in [2,3,5]:
            while num % x == 0:
                num //= x
        return num == 1

if __name__ == '__main__':
    s = Solution()
    s.isUgly(6)