class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for s_l in s:
            ans = ans * 26 + ord(s_l) - ord('A') + 1
        return ans