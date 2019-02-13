class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []: return []
        ret = []
        n, m = len(matrix), len(matrix[0])
        maxUp, maxLeft, maxDown, maxRight = 0, 0, n-1, m-1
        direction = 0
        while True:
            if direction == 0:
                for i in range(maxLeft, maxRight+1):
                    ret.append(matrix[maxUp][i])
                maxUp += 1
            if direction == 1:
                for i in range(maxUp,maxDown+1):
                    ret.append(matrix[i][maxRight])
                maxRight -=1
            if direction == 2:
                for i in reversed(range(maxLeft,maxRight+1)):
                    ret.append(matrix[maxDown][i])
                maxDown -= 1
            if direction == 3:
                for i in reversed(range(maxUp, maxDown+1)):
                    ret.append(matrix[i][maxLeft])
                maxLeft += 1
            if maxUp > maxDown or maxLeft > maxRight:
                return ret
            direction = (direction+1)%4