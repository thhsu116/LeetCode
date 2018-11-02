# https://leetcode.com/problems/palindrome-number/description/

# converting INT to STR
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        if x == int(str(x)[-1::-1]):
            return True
        else:
            return False
            
# reverse INT without converting to STR
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        
        x_copy = x
        x_rev = 0
        while x > 0:
            temp = x % 10
            x_rev = x_rev*10 + temp
            x = x // 10
        if x_copy == x_rev:
            return True
        else:
            return False
            
