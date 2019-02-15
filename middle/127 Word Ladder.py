class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def isValid(word, nextWord):
            ret = 0
            for i in range(len(word)):
                if ret > 1: return False
                if word[i] != nextWord[i]:
                    ret += 1
            return ret == 1
        dct = {}
        self.ret = len(wordList) + 1
        def travel(dct, cnt, nowWord):
            if cnt > len(wordList): return
            if isValid(nowWord, endWord):
                print(nowWord)
                self.ret = min(self.ret, cnt)
            for i in range(len(wordList)):
                if isValid(nowWord, wordList[i]) and \
                        (i not in dct or dct[i] == 0):
                    dct[i] = 1
                    travel(dct, cnt+1, wordList[i])
                    dct[i] = 0
        travel(dct, 0, beginWord)
        return self.ret + 2 if self.ret == len(wordList)+1 else 0