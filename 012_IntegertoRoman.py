# https://leetcode.com/problems/integer-to-roman/description/

# 99% 112ms, implement conversion rules for each digit
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ''
        digit = num // 1000
        if digit > 0:
            ans += 'M' * digit
            num -= digit * 1000

        digit = num //100
        if digit > 0:
            if digit == 9:
                ans += 'CM'
            elif digit == 4:
                ans += 'CD'
            elif digit >= 5:
                ans += 'D' + 'C'*(digit-5)
            else:
                ans += 'C'*digit
            num -= digit*100
        
        digit = num //10
        if digit > 0:
            if digit == 9:
                ans += 'XC'
            elif digit == 4:
                ans += 'XL'
            elif digit >= 5:
                ans += 'L' + 'X'*(digit-5)
            else:
                ans += 'X'*digit
            num -= digit*10
        
        digit = num
        if digit == 9:
            ans += 'IX'
        elif digit == 4:
            ans += 'IV'
        elif digit >= 5:
            ans += 'V' + 'I'*(digit-5)
        else:
            ans += 'I'*digit
        
        return ans
        
# iterative solution
        result = ''
        d = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),  (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        for one_tuple in d:
            while num >= one_tuple[0]:
                result += one_tuple[1]
                num -= one_tuple[0]
        return result
