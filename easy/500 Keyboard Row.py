from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        lst = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

        def check(s):
            s = s.lower()
            #print(s)
            i = -1
            for index, st in enumerate(lst):
                if s[i] in st:
                    i = index
                    break
            for st in s:
                if st not in lst[i]:
                    return False
            return True

        res = []
        for word in words:
            if check(word):
                res.append(word)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
