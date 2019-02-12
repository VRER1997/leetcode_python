class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        strs = s.strip(' ').split(' ')
        return len(strs[-1])

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("a  "))