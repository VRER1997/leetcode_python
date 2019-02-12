class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        maxl = 0
        start = 0
        for i in range(n):
            print("i=%d maxl=%d start=%d" % (i,maxl,start))
            # 试图判断还有没有更长的
            if i - maxl >= 1 and s[i - maxl - 1: i + 1] == s[i - maxl - 1: i + 1][::-1]:
                start = i - maxl - 1
                maxl += 2
                continue
            # 试图找到一个子字符串，若存在则是当前最长的
            if i - maxl >= 0 and s[i - maxl: i + 1] == s[i - maxl: i + 1][::-1]:
                start = i - maxl
                maxl += 1
        return s[start: start + maxl]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("adda"))