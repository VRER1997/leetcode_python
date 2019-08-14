from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = nums1
        s.sort()
        nums2.sort()
        i, j, dit = 0, 0, {}
        while i < len(s) and j < len(nums2):
            if s[i] >= nums2[j]:
                j += 1
            else:
                dit[s[i]] = nums1[j]
                i += 1
        if j == len(nums2):
            for k in range(i, len(s)):
                dit[s[k]] = -1
        print(dit)
        res = []
        for i in range(len(nums1)):
            res.append(dit[nums1[i]])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))