class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n, m = len(matrix), len(matrix[0]) if matrix else 0
        if n == 0 or m == 0: return False
        flag = 2**31-1
        def binarySearch(nums, r):
            l = 0
            while l <= r:
                mid = l + ((r-l)>>2)
                if nums[mid] == target: return flag
                elif nums[mid] > target: r = mid-1
                else: l = mid+1
            return r
        i = binarySearch([matrix[i][0] for i in range(n)],n-1)
        print(binarySearch(matrix[i][:]))
        return i == flag or binarySearch(matrix[i][:],m-1) == flag

if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([
        [1,3,5,7],
        [10,11,16,20],
        [23,30,34,50]],3))