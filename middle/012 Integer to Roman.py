class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dct = {1000:'M', 900: 'CM', 500:'D', 400:'CD', 100:'C', 90: 'XC',
               50:'L', 40:'XL', 10: 'X', 9:'IX', 5:'V', 4: 'IV', 1:'I' }
        ret = ''
        for key in dct.keys():
            while num - key >= 0:
                ret += dct[key]
                num -= key
        return ret
if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(1994))