class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct = {}
        for char in s:
            if char not in dct:
                dct[char] = 1
            else:
                dct[char] += 1
        ret, w = 0, 0
        for key, value in dct.items():
            w += value % 2
            ret += value if value % 2 == 0 else value-1
        return ret + (1 if w > 0 else 0)
