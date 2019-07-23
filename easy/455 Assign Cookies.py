from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i, j, cnt = 0, 0, 0
        s.sort()
        g.sort()
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                j += 1
                cnt += 1
            else:
                j += 1
        return cnt