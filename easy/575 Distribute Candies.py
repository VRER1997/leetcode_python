from typing import List
from collections import Counter
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        can = Counter(candies)
        sz, canNum = len(can), len(candies)//2
        return sz if sz <= canNum else canNum

    #        return min(len(set(candies)), len(candies) // 2)


if __name__ == '__main__':
    s = Solution()
    print(s.distributeCandies(candies = [1,1,2,3]))