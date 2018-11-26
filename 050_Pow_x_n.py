# https://leetcode.com/problems/powx-n/

# 9% 63ms
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def quickPow(y, m):
            po = 1
            prod = y
            while po*2 < m:
                prod *= prod
                po *= 2
            return (prod, po)
        
        if x == 0:
            return 0
        elif x == 1:
            return 1
        
        if n == 1:
            return x
        elif n == 0:
            return 1
        
        ret = 1
        remain_n = abs(n)
        while remain_n:
            prod, m = quickPow(x, remain_n)
            ret *= prod
            remain_n -= m
            
        if n < 0:
            return 1/ret
        else:
            return ret
            
# 92% 40ms, recursive
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 1:
            return x
        elif n == 0:
            return 1
        elif n == -1:
            return 1/x
        
        if x == 0:
            return 0
        elif x == 1:
            return 1
        
        half = self.myPow(x, int(n/2))  # -3 // 2 = -2, so use int() to get integar part
        #print(half)
        if n % 2 == 0:
            return half * half
        elif n > 0:
            return half * half * x
        else:
            return half * half / x
