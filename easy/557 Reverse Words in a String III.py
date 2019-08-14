class Solution:
    def reverseWords(self, s: str) -> str:
        return ''.join(sli[::-1] for sli in s.split(' '))