# https://leetcode.com/problems/unique-paths-ii/

# 44ms 46%, dynamic programing, count unique paths from the end, set unique paths to 0 on obstacle grids
# time complexity O(m*n), space complexity O(m*n) => reuse obstacleGrid to turn space complexity to O(1)
# https://leetcode.com/problems/unique-paths-ii/solution/
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        h = len(obstacleGrid)
        w = len(obstacleGrid[0])
        rec = {(h-1, w-1): 1}
        for c in range(w-1, -1, -1):
            for r in range(h-1, -1, -1):
                if r < h - 1 or c < w - 1:
                    rec[(r, c)] = 0
                if obstacleGrid[r][c] == 0:
                    if r < h - 1:
                        rec[(r, c)] = rec[(r, c)] + rec[(r + 1, c)]
                    if c < w - 1:
                        rec[(r, c)] = rec[(r, c)] + rec[(r, c + 1)]
                else:
                    rec[(r, c)] = 0
        return rec[(0, 0)]
