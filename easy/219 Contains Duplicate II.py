class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dct = {}
        for index, num in enumerate(nums):
            if num in dct:
                if index-dct[num] <= k:
                    return True
            dct[num] = index
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate([1,0,1,1], 1))