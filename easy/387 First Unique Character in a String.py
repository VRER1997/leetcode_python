class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct = dict()
        for index,char in enumerate(s):
            if char in dct:
                dct[char] = -1
            else:
                dct[char] = index
        for key,value in dct.items():
            if value != -1:
                return key
        return -1

if __name__ == '__main__':
    s = Solution()
    s.firstUniqChar('leetcode')