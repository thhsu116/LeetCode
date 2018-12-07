# https://leetcode.com/problems/plus-one/

# 36ms 99%, time complexity O(n), space complexity O(1)
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits) - 1
        co = 1
        while n >= 0:
            num = digits[n] + co
            digits[n] = num % 10
            co = num // 10
            if not co:
                break
            n -= 1
        if co:
            return [1] + digits
        else:
            return digits
