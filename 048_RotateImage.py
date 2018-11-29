# https://leetcode.com/problems/rotate-image/

# 36ms 99%
# 1. starting from left most element of row 0, swap 4 elements, then move on to next element on the right
# 2. repeat 1 until 2nd last element of row 0, this way, all elements on the edge of square are swaped
# 3. set starting point to 2nd element of row 2, does swaping as 1 until 2ns last element of the row
# 4. set starting point to 3rd elemnet of row 3, repeat the sawping
# 5. keep repeating until reaching the center of the matrix
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        x, y = 0, 0  # starting index of each iteration
        while n > 1:
            for i in range(n-1):
                matrix[y+i][x+n-1], \
                matrix[y+n-1][x+n-1-i], \
                matrix[y+n-1-i][x], \
                matrix[y][x+i] = \
                matrix[y][x+i], \
                matrix[y+i][x+n-1], \
                matrix[y+n-1][x+n-1-i], \
                matrix[y+n-1-i][x]
            x += 1
            y += 1
            n -= 2
