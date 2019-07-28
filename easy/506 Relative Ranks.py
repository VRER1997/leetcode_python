from typing import List
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        numcpy = nums.copy()
        numcpy.sort(reverse=True)
        dct = {}
        for index, value in enumerate(numcpy):
            if index == 0:
                dct[value] = 'Gold Medal'
            elif index == 1:
                dct[value] = 'Silver Medal'
            elif index == 2:
                dct[value] = 'Bronze Medal'
            else:
                dct[value] = str(index+1)
        res = []
        for a in nums:
            res.append(dct[a])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.findRelativeRanks([5, 4, 2, 3, 1]))