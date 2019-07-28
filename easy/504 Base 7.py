class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ""
        if num < 0:
            res += '-'
        if num == 0:
            return '0'
        t, num = [], abs(num)
        while num:
            t.append(str(num%7))
            num = num // 7
        res += ''.join(t[::-1])

        return res