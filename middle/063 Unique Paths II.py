class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        '''
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        cache = {}

        def dfs(x,y):
            if (x,y) in cache:
                return cache[x,y]

            ret = 0
            if x == n - 1 and y == m - 1: ret = 1
            if obstacleGrid[x][y] == 0:
                if x+1 < n: ret += dfs(x+1, y)
                if y+1 < m: ret += dfs(x, y+1)
            cache[x,y] = ret
            return cache[x,y]

        if obstacleGrid[0][0]: return 0
        return dfs(0,0)
        '''
        n, m = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] : return 0
        obstacleGrid[0][0] = 1
        for i in range(1,n):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)
        for i in range(1,m):
            obstacleGrid[0][i] = int(obstacleGrid[0][i] == 0 and obstacleGrid[0][i-1] == 1)
        #print(obstacleGrid)
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[n-1][m-1]
