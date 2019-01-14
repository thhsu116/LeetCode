# https://leetcode.com/problems/word-search/

# 476 ms 22%, DFS 
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def find_word(board, word, i, j, record):
            for r, c in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                    continue
                if board[r][c] == word[0] and (r, c) not in record:
                    if len(word) == 1:
                        return True
                    else:
                        #print(record+[(r, c)])
                        if find_word(board, word[1:], r, c, record+[(r, c)]):
                            return True
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    elif find_word(board, word[1:], i, j, [(i, j)]):
                        return True
        return False
 
 # 180ms, 100% solution
 class Solution:
    
    def search(self, board, word, idx, row, col):
        if idx == len(word) - 1:
            return True
        
        board[row][col] = ''
        char = word[idx + 1]
        
        if col > 0 and board[row][col - 1] == char and self.search(board, word, idx + 1, row, col - 1):
            return True        
        if row > 0 and board[row - 1][col] == char and self.search(board, word, idx + 1, row - 1, col):
            return True
        if col < len(board[0]) - 1 and board[row][col + 1] == char and self.search(board, word, idx + 1, row, col + 1):
            return True
        if row < len(board) - 1 and board[row + 1][col] == char and self.search(board, word, idx + 1, row + 1, col):
            return True
        
        board[row][col] = word[idx]
        
        return False
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        first = word[0]
        
        for row in range(len(board)):
            for col in range(len(board[row])):                
                if board[row][col] == first:
                    if self.search(board, word, 0, row, col):
                        return True
            
        return False
