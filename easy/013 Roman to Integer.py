class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        mapping = {'#':0, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}
        s_l = s + '#'
        for i in range(len(s)):
            if mapping[s_l[i]] >= mapping[s_l[i+1]]:
                res += mapping[s_l[i]]
            else:
                res -= mapping[s_l[i]]
        print(res)
        return res

if __name__ == '__main__':
    s = Solution()
    s.romanToInt('IV')
