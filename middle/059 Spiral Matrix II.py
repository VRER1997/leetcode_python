class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1: return [[1]]
        maxup,maxleft,maxdown,maxright = 0,0,n-1,n-1
        direction = 0
        board = []
        for i in range(n):
            board.append([0 for j in range(n)])
        cnt = 1
        while True:
            if direction == 0:
                for i in range(maxleft,maxright+1):
                    board[maxup][i] = cnt
                    cnt += 1
                maxup += 1

            if direction == 1:
                for i in range(maxup, maxdown+1):
                    board[i][maxright] = cnt
                    cnt += 1
                maxright -= 1

            if direction == 2:
                for i in reversed(range(maxleft,maxright+1)):
                    board[maxdown][i] = cnt
                    cnt += 1
                maxdown -= 1

            if direction == 3:
                for i in reversed(range(maxup,maxdown+1)):
                    board[i][maxleft] = cnt
                    cnt += 1
                maxleft += 1

            if maxleft > maxright: return board
            direction = (direction + 1) % 4
if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(6))