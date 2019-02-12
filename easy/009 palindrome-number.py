class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        l, i = len(str_x), 0
        while i < l//2:
            if str_x[i] != str_x[l-i-1]:
                return False
        return True