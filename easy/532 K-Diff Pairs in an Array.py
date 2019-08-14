from typing import List
import collections
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        if k < 0: return 0
        elif k == 0:
            count = collections.Counter(nums)
            for v, k in count.items():
                if k >= 2:
                    res += 1
            return res
        else:
            nums = set(nums)
            for num in nums:
                if num+k in nums:
                    res += 1
            return res


if __name__ == '__main__':
    s = Solution()
    print(s.findPairs([3, 1, 4, 1, 5], k = 2))