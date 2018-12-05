# https://leetcode.com/problems/n-queens-ii/

# 88ms, 58%, DFS, iterate through each column, if queen is valid on a row, go to next column
# https://www.youtube.com/watch?v=0DeznFqrgAI
class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        ANS = []
        
        def safe(board, r, c):
            n = len(board)
            if sum(board[r]) >= 1:
                return False
            i, j = r, c
            while i >= 0 and j >= 0:
                if board[i][j]:
                    return False
                i, j = i-1, j-1
            
            i, j = r, c
            while i < n and j >= 0:
                if board[i][j]:
                    return False
                i, j = i+1, j-1
            return True

        
        def solveNQueens(board, col):
            ans = 0
            for i in range(len(board)):
                #print(board)
                if safe(board, i, col):
                    board[i][col] = 1
                    if col == n-1:
                        #print(board)
                        #ANS.append(board)
                        ans += 1
                    else:
                        #ans += solveNQueens(board, col+1)
                        ans += solveNQueens(board, col+1)
                    board[i][col] = 0
            return ans
        
        res = 0
        for i in range(n):
            board = [[0 for _ in range(n)] for _ in range(n)]
            board[i][0] = 1
            #print(board)
            res += solveNQueens(board, 1)
            #solveNQueens(board, 1)
        return res
        #return len(ANS)
