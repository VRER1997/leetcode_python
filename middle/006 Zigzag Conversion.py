class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        if numRows == 1: return s
        cl = n // (2*numRows-2) * (numRows-1)
        t = n % (2*numRows-2)
        if 0 < t <= numRows: cl += 1
        if  numRows < t: cl += (t-numRows+1)

        ret = []
        for i in range(numRows):
            ret.append([-1 for j in range(cl)])
        cnt, x, y = 0, 1, -1
        while cnt < n:
            t = cnt % (2*numRows-2)
            if 0 < t <= numRows-1: x += 1
            else:
                y += 1
                x -= 1
            ret[x][y] = cnt
            cnt += 1

        r = ''
        for i in range(numRows):
            for j in range(cl):
                r += (s[ret[i][j]] if ret[i][j] >= 0 else '')
        return r

if __name__ == '__main__':
    s = Solution()
    print(s.convert("", 1))