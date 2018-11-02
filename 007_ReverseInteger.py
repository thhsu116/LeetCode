# https://leetcode.com/problems/reverse-integer/description/

# using python str
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(x)
        if x_str.startswith('-'):
            x_rev = -1*int(x_str[-1:0:-1])
        else:
            x_rev = int(x_str[-1::-1])
            
        if x_rev > 2**31 - 1 or x_rev < -1*2**31:
            return 0
        else:
            return x_rev

# using mod 10
class Solution(object):
    def reverse(self, x):
        isNegative = False
        if x < 0:
            isNegative = True
            x = x * (-1)
        num = 0    
        while x > 0:
            temp = x % 10
            #print(temp)
            num = num * 10 + (temp)        
            x = x // 10
        if isNegative:
            if (-1 * num) < (-2 ** 31):
                return 0
            return (-1 * num)
        else:
            if num > (2**31 - 1):
                return 0
            return num
