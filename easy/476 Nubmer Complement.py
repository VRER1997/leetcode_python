class Solution:
    def findComplement(self, num: int) -> int:
        if num == 1:
            return 0
        s = bin(num)[2:]
        #print(s)
        s = ['1' if s[i] == '0' else '0' for i in range(len(s))]
        i = 0
        while s[i] == '0': i+=1
        s = s[i:][::-1]
        #print(s)
        res, x = 0, 1
        for i in range(len(s)):
            if s[i] == '1':
                res += x
            x *= 2
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findComplement(1))