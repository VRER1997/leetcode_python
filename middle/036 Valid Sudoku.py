class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # visit python实现
        for i in range(9):
            col, row = {}, {}
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    row[board[i][j]] = 1
                if board[j][i] != '.':
                    if board[j][i] in col:
                        return False
                col[board[j][i]] = 1
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.check(board, i, j):
                    return False
        print(123)
        return True

    def check(self, board, x, y):
        unit = {}
        for i in range(x, x+3):
            for j in range(y, y+3):
                if board[i][j] != '.':
                    if board[i][j] in unit:
                        return False
                    unit[board[i][j]] = 1
        return True

if __name__ == '__main__':
    s = Solution()
    board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]]
    s.isValidSudoku(board)

