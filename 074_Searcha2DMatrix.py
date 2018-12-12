# https://leetcode.com/problems/search-a-2d-matrix/

# 36ms 100%, time complexity O(m+n), space complexity O(1)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        for i in range(len(matrix) - 1):
            if matrix[i][0] <= target and matrix[i+1][0] > target:
                return target in matrix[i]
        return target in matrix[-1]
        
# can also use two binary search
