# https://leetcode.com/problems/spiral-matrix/

# 32ms 100%, time complexity: O(max(m, n)), space complexity O(m*n)
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        w = len(matrix[0])
        if w == 1:
            return [m[0] for m in matrix]
        l = len(matrix)
        if l == 1:
            return matrix[0]
        res = [0] * (w * l)
        start = 0
        x, y = 0, 0
        while w > 0 and l > 0:
            #print('{} {}'.format(w, l))
            try:
                for i in range(w):
                    res[start + i] = matrix[y][x + i]
                    res[start + w + l - 2 + i] = matrix[y + l - 1][x + w - 1 - i]
                for i in range(l):
                    res[start + w - 1 + i] = matrix[y + i][x + w - 1] 
                    if i < l-1:
                        res[start + 2*w + l -3 + i] = matrix[y + l - 1 - i][x]
            except:
                break
            start += 2*w + 2*l - 4
            x += 1
            y += 1
            w -= 2
            l -= 2
        return res
