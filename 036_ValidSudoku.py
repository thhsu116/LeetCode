# https://leetcode.com/problems/valid-sudoku/description/

# 12% 116ms, brute force with Counter
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        from collections import Counter
        # validate row
        for i in range(9):
            counter = Counter(board[i])
            if not all(v == 1 for k, v in counter.items() if k.isdigit()):
                return False
        
        # validate column
        for x in range(9):
            counter = Counter([board[y][x] for y in range(9)])
            if not all(v == 1 for k, v in counter.items() if k.isdigit()):
                return False
        
        # validated 3x3
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                counter = Counter([board[i + y%3][j + y//3] for y in range(9)])
                if not all(v == 1 for k, v in counter.items() if k.isdigit()):
                    return False
        
        return True
        
 # 40% 80ms, brute force wiht set() to keep record
 class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        record = set()
        # validate row
        for i in range(9):
            record.clear()
            for n in board[i]:
                if n in record:
                    return False
                elif n.isdigit():
                    record.add(n)
        
        # validate column
        for x in range(9):
            record.clear()
            for y in range(9):
                n = board[y][x]
                if n in record:
                    return False
                elif n.isdigit():
                    record.add(n)
        
        # validated 3x3
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                record.clear()
                for y in range(9):
                    n = board[i + y%3][j + y//3]
                    if n in record:
                        return False
                    elif n.isdigit():
                        record.add(n)
        
        return True
        
# iterate each number, use some coding to record locations of the number(ex: n in row: x, column: y, 3x3: z)
# return False if location is alreadu in record
