# https://leetcode.com/problems/unique-paths/

# 36ms 94%
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        from math import factorial
        
        total = m - 1 + n - 1
        return int(factorial(total)/(factorial(m -1) * factorial(n - 1)))
