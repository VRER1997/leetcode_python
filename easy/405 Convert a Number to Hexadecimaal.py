class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ''
        alpha = '0123456789abcdef'
        if num == 0:
            return '0'
        while num != 0 and len(result) < 8:
            result += alpha[num & 0xf]
            num >>= 4
        return result[::-1]