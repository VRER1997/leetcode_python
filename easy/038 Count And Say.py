class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "21"
        if n == 1: return s
        for j in range(n-1):
            t, w, next_s = 0, s[0], ''
            for i in range(len(s)):
                if s[i] == w: t += 1
                else:
                    next_s += (str(t) + w)
                    t = 1
                    w = s[i]
                if i+1 == len(s):
                    next_s += (str(t) + w)
            s = next_s

        return s

if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(3))