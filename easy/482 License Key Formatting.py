class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        strs = S.split('-')
        s = ''.join(strs)[::-1]
        t = ''
        for i in range(len(s)):
            t += s[i].upper()
            if i % K == K-1 and i < len(s)-1:
                t += '-'
        return t[::-1]

if __name__ == '__main__':
    s = Solution()
    print(s.licenseKeyFormatting(S = "2-5g-3-J", K = 2))