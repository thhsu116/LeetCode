# https://leetcode.com/problems/minimum-path-sum/

# 80ms 29%, dynamic programming
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0])
        for r in range(h):
            for c in range(w):
                up, left = float('inf'), float('inf')
                if r > 0:
                    up = grid[r - 1][c]
                if c > 0:
                    left = grid[r][c - 1]
                if r > 0 or c > 0:
                    grid[r][c] = grid[r][c] + min(up, left)
                
        #print(grid)
        return grid[h - 1][w - 1]
