class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if 0 <= num < 10: return num
        cnt = 0
        while num:
            mod = num % 10
            cnt += mod
            num //= 10
        return self.addDigits(cnt)