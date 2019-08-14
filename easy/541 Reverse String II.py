class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        for i in range(0, len(s), 2*k):
            res.append(s[i:i+k][::-1] + s[i+k:i+2*k])
        return ''.join(res)

if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr(s = "abcdefg", k = 9))

