class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        strings = s.strip().split()
        return ' '.join(strings[::-1])


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords(" the  sky is blue"))