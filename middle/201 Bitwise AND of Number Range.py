class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d = 0
        while m != n:
            m >>= 1
            n >>= 1
            d += 1
        return m << d