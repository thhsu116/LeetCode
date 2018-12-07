# https://leetcode.com/problems/climbing-stairs/

# 36ms 70%
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def fac(m):
            ret = 1
            while m > 1:
                ret *= m
                m -= 1
            return ret
            
        
        strides = n
        twos = 0
        ret = 0
        while strides >= twos:
            ret += fac(strides)/(fac(strides-twos)*fac(twos))
            strides -= 1
            twos += 1
        return int(ret)
