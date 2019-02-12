class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s : return 0
        i, t, cnt = 0, ' ', 0
        while i < len(s) and s[i] == t: i+=1
        while i < len(s):
            if t == ' ' and s[i] == t:
                cnt += 1
                t = 'a'
            if t == 'a' and s[i] != ' ':
                t = ' '
            i += 1
        return cnt + (s[-1] != ' ')

if __name__ == '__main__':
    s = Solution()
    print(s.countSegments("                "))