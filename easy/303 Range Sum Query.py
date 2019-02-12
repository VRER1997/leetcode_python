class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum = [0]
        for num in nums:
            self.sum.append(num+self.sum[-1])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum[j+1]-self.sum[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)