# https://leetcode.com/problems/sudoku-solver/

# 12% 1432ms, DFS by adding potential answers to empty grid and validating it
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def is_valid(board, i, j):
            for col in range(9):
                if j != col and board[i][j] == board[i][col]:
                    return False
            for row in range(9):
                if i != row and board[i][j] == board[row][j]:
                    return False
            for x in range(i//3*3, i//3*3+3):
                for y in range(j//3*3, j//3*3+3):
                    if (x, y) != (i, j) and board[x][y] == board[i][j]:
                        return False
            return True
        
        def dfs(board, i, j):
            if i == 9:
                return True
            if j >= 9:
                return dfs(board, i+1, 0)
            if board[i][j] == '.':
                for k in range(1, 10):
                    board[i][j] = str(k)
                    if is_valid(board, i, j):
                        if dfs(board, i, j+1):
                            return True
                    board[i][j] = '.'
            else:
                return dfs(board, i, j+1)
            return False
        
        dfs(board, 0, 0)
        
# DFS with starting from grid with fewest potential answers
# https://leetcode.com/problems/sudoku-solver/discuss/15759/48ms-straitforward-python-DFS-solution-with-explanations
