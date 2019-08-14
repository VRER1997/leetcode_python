import collections

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        if len(s) < len(p):
            return res
        maps = collections.Counter(p)
        cnt = len(maps.keys())
        begin, end = 0, 0
        while end < len(s):
            if s[end] in maps:
                maps[s[end]] -= 1
                if maps[s[end]] == 0:
                    cnt -= 1
            end += 1
            while cnt == 0:
                if s[begin] in maps:
                    if maps[s[begin]] == 0:
                        cnt += 1
                    maps[s[begin]] += 1
                if end - begin == len(p):
                    res.append(begin)
                begin += 1
        return res