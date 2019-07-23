class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def check(s, sub):
            if len(s) % len(sub) != 0:
                return False
            for i in range(len(s)):
                if s[i] != sub[i%len(sub)]:
                    return False
            return True

        l, r = 0, 10005
        for i in range(1, len(s)):
            if check(s, s[:i]):
                return True
        return False
