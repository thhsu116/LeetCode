# https://leetcode.com/problems/set-matrix-zeroes/

# 144ms, time: O(mn), space: O(m+n)
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows_to_zeros = set()
        cols_to_zeros = set()
        m = len(matrix)
        n = len(matrix[0])
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row not in rows_to_zeros:
                        rows_to_zeros.add(row)
                    if col not in cols_to_zeros:
                        cols_to_zeros.add(col)
                    
        for row in rows_to_zeros:
            matrix[row] = [0] * n
        for col in cols_to_zeros:
            for r in range(m):
                matrix[r][col] = 0

# 148ms, time: O((M×N)×(M+N)), space: O(1)
        m = len(matrix)
        n = len(matrix[0])
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    for c in range(n):
                        if matrix[row][c] != 0 and matrix[row][c] != 'z':
                            matrix[row][c] = 'z'
                    for r in range(m):
                        if matrix[r][col] != 0 and matrix[r][col] != 'z':
                            matrix[r][col] = 'z'
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 'z':
                    matrix[row][col] = 0
# 140ms, time O(mn), space O(1)
# approach 3 in https://leetcode.com/problems/set-matrix-zeroes/solution/
def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        is_col = False
        for row in range(m):
            if matrix[row][0] == 0:
                is_col = True
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
                    
        for row in range(1, m):
            for col in range(1, n):
                if not matrix[row][0] or not matrix[0][col]:
                    matrix[row][col] = 0
        
        if matrix[0][0] == 0:
            matrix[0] = [0] * n
        
        if is_col:
            for row in range(m):
                matrix[row][0] = 0
