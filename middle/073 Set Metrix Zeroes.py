class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0]) if matrix else 0
        col, row = set(), set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    col.add(i)
                    row.add(j)
        for i in range(n):
            for j in range(m):
                if i in col or j in row:
                    matrix[i][j] = 0