# https://leetcode.com/problems/gray-code/

# 56ms 92%, recursive
class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def get_gray_code(n):
            if n == 1:
                return ['0', '1']
            codes = get_gray_code(n-1)
            return ['0' + c for c in codes] + ['1' + c for c in codes[-1::-1]]
        
        if n == 0:
            return [0]
        else:
            return [int(c, 2) for c in get_gray_code(n)]

# 52ms 98%, iterative
class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """        
        codes = [0]
        for i in range(1, n+1):
            codes = [0 | c for c in codes] + [(1 << i-1) | c for c in codes[-1::-1]]
        return codes
        
# other approaches:
http://www.cnblogs.com/grandyang/p/4315649.html
