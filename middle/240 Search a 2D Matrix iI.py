class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix :
            return False

        n, m = len(matrix), len(matrix[0])
        i, j = 0, m-1
        while i < n and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] == target:
                return True
            else:
                j -= 1
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([[1,   4,  7, 11, 15],
                          [2,   5,  8, 12, 19],
                          [4,   6,  9, 16, 22],
                          [10, 13, 14, 17, 24],
                          [18, 21, 23, 26, 30]], 3))