class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sp = self.getPatten(s)
        st = self.getPatten(t)
        return sp == st

    def getPatten(self, s):
        dct, p, cnt = {}, '', 0
        for char in s:
            if char not in dct:
                dct[char] = cnt
                cnt += 1
            p += str(dct[char])
        return p

if __name__ == '__main__':
    s = Solution()
    print(s.getPatten("add"))