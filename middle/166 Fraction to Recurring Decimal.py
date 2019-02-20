class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'
        ret = '-' if numerator * denominator < 0 else ''

        numerator, denominator = abs(numerator), abs(denominator)
        ret += str(numerator//denominator)
        if numerator % denominator == 0:
            return ret

        ret += '.'
        r = numerator % denominator
        m = {}
        while r: #simulate the division process
            if r in m:
                ret = ret[:m[r]] + '(' + ret[m[r]:] + ')'
                break
            m[r] = len(ret)
            r *= 10
            ret += str(r//denominator)
            r %= denominator
        return ret
