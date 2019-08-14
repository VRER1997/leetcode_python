from typing import List
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not nums: return nums
        n, m = len(nums), len(nums[0])
        if n*m != r*c:
            return nums
        count, res = 0, []
        for i in range(n):
            for j in range(m):
                if count % c == 0:
                    res.append([nums[i][j]])
                else:
                    res[-1].append(nums[i][j])
                count += 1
        return res