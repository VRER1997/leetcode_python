class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0]) if board else 0

        def mark(x, y):
            if 0 <= x < n and 0 <= y < m:
                if board[x][y] == 'O':
                    board[x][y] = '#'
                    mark(x + 1, y)
                    mark(x - 1, y)
                    mark(x, y + 1)
                    mark(x, y - 1)

        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    if board[i][j] == 'O':
                        mark(i, j)
        # print(board)
        for i in range(n):
            for j in range(m):
                board[i][j] = 'O' if board[i][j] == '#' else 'X'