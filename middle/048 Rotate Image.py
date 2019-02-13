class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        def _ratate(n, start):
            if n == 0: return
            if n == 1: return
            print(n)
            print(matrix)
            for i in range(start, start + n-1):
                # self.r(matrix[start][i], matrix[i][n-start-1], matrix[n-start-1][n-start-i-1],\
                # matrix[n-start-i-1][start])
                ''' start = 0 n = 4
                    0      1     2     3
                  [0,0]  [0,1]  [0,2] [0,3]
                  [0,3]  [1,3]  [2,3] [3,3]
                  [3,3]  [3,2]  [3,1]
                  [3,0]  [2,0]  [1,0]
                  
                  n = 2 start = 1
                  
                '''
                print(n, start)
                print(matrix[start][i], matrix[i][n-start-1], matrix[n-start-1][n + start-i-1],matrix[n+start-i-1][start])
                print([start,i], [i,n-start-1], [n-start-1, n + start-i-1], [n+start-i-1, start])
                matrix[start][i], matrix[i][n-start-1], matrix[n-start-1][n + start-i-1],matrix[n+start-i-1][start] = \
                matrix[n+start-i-1][start], matrix[start][i], matrix[i][n-start-1], matrix[n-start-1][n+start-i-1]
                print(matrix)


            _ratate(n-2, start+1)
        _ratate(n,0)
if __name__ == '__main__':
    s = Solution()
    matrix = [[ 5, 1, 9,11],
              [ 2, 4, 8,10],
              [13, 3, 6, 7],
              [15,14,12,16]]
    s.rotate(matrix)
    print(matrix)