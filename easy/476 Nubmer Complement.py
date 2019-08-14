class Solution:
    def findComplement(self, num: int) -> int:
        s = bin(num)[2:]
        s = ['1' if s[i] == '0' else '0' for i in range(len(s))]
        #print(s)
        i = 0
        while i < len(s) and s[i] == '0': i+=1
        if i == len(s):
            return 0
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