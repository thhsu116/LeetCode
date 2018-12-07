# https://leetcode.com/problems/n-queens/

# 112ms 54%
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 1:
            return [['Q']]
        
        ANS = []
        
        def safe(board, r, c):
            n = len(board)
            if 'Q' in board[r]:
                return False
            i, j = r, c
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i, j = i-1, j-1
            
            i, j = r, c
            while i < n and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i, j = i+1, j-1
            return True
        
        def dfs(board, col):
            ans = 0
            for i in range(len(board)):
                if safe(board, i, col):
                    board[i][col] = 'Q'
                    if col == len(board)-1:
                        ANS.append([''.join(r) for r in board])
                        ans += 1
                    else:
                        ans += dfs(board, col+1)
                    board[i][col] = '.'  # reset board for next iteration
            return ans
        
        res = 0
        for i in range(n):
            board = [['.' for _ in range(n)] for _ in range(n)]
            board[i][0] = 'Q'
            res += dfs(board, 1)

        return ANS
