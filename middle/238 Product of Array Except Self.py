from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        l, r = [1], [1]
        n = len(nums)
        for i in range(n-1):
            l.append(l[-1]*nums[i])
            r.append(r[-1]*nums[n-i-1])

        output = []
        r = r[::-1]
        for i in range(n):
            output.append(l[i]*r[i])

        return output

if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))