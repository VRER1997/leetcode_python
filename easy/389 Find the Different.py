import re
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for char in s:
            str_t, _ = re.subn( char, '', t, count=1)
            t = str_t
        return t
