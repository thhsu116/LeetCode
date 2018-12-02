# https://leetcode.com/problems/spiral-matrix-ii/

# 36ms, 99%, time complexity O(n), space complexity O(n^2)
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for _ in range(n)]
        x, y = 0, 0
        side = n
        start = 1
        while side > 0:
            for i in range(side):
                #print('{} {}'.format(x, y))
                res[y][x + i] = start + i
                res[y + i][x + side -1] = start + side - 1 + i
                res[y + side-1][x + side - 1 -i] = start + 2*(side - 1) + i
                if i < side - 1:
                    res[y + side - 1 - i][x] = start + 3*(side - 1) + i
            start += 4*(side - 1)
            x += 1
            y += 1
            side -= 2
        return res
