# https://leetcode.com/problems/sqrtx/

# 60ms 82%, binary search
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        
        l = 0
        r = x
        while True:
            c = (l + r) // 2  # stay with int for faster calculation
            if c * c == x:
                return c
            elif c * c < x:
                if (c + 1) ** 2 > x:
                    return c
                l = c
            else:
                r = c

# Newton's method
# https://en.wikipedia.org/wiki/Newton%27s_method
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        elif x == 0:
            return 0
        
        last = 0
        cur = 1
        while True:
            last = cur
            cur = (cur + x/cur)/2
            if int(last) == int(cur):
                return int(last)
