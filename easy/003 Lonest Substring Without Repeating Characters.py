class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        set = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in set:
                i = max(i, set[s[j]])
            ans = max(ans, j-i+1)
            set[s[j]] = j+1

        return ans