from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        s = e = nums[0]
        i, res = 1, []
        while i < len(nums):
            if nums[i] == e+1:
                e += 1
            else:
                if s == e:
                    res.append(str(s))
                else:
                    res.append(str(s) + "->" + str(e))
                s = e = nums[i]
            i += 1

        if s == e:
            res.append(str(s))
        else:
            res.append(str(s) + "->" + str(e))
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.summaryRanges([0,2,3,4,6,8,9]))