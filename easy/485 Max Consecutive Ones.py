from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, num, cnt = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                if l == 0:
                    l = 1
                num += 1
            if nums[i] == 0:
                if l == 1:
                    cnt = max(num, cnt)
                    num = 0
        if l == 1:
            cnt = max(num, cnt)
        return cnt
if __name__ == '__main__':
    s = Solution()
    print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))