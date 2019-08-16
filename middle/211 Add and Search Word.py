import string
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = []

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.dict.append(word)

    # Time Exceede Limits
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        n = len(word)
        def dfs(wordG, cur):
            if cur == n:
                #print(wordG)
                return self.dict.count(wordG)
            if word[cur] != '.':
                return dfs(wordG, cur+1)
            for w in string.ascii_lowercase:
                #wordG[cur] = w
                wordG = wordG[:cur] + w + wordG[cur+1:]
                if dfs(wordG, cur+1):
                    return True
            return False

        return dfs(word, 0)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('word')
obj.addWord('sord')
param_2 = obj.search('...f')
print(param_2)