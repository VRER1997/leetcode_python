class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        def checkAllUpperOrLower(w: str):
            for s in w:
                if s.isupper() != w[0].isupper():
                    return False
            return True

        if checkAllUpperOrLower(word):
            return True
        if len(word) > 1 and word[0].isupper() and checkAllUpperOrLower('a'+word[1:]):
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.detectCapitalUse('FlaG'))