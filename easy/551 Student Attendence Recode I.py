class Solution:
    def checkRecord(self, s: str) -> bool:
        i, j = 0, 0
        for k in range(len(s)):
            if s[k] == 'A':
                i += 1
            if i > 1:
                return False
            if s[k] == 'L' and k < len(s)-2 and s[k+1] == 'L' and s[k+2] == 'L':
                return False
        return True