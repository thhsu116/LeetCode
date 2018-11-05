# https://leetcode.com/problems/roman-to-integer/description/

# 99%, 120ms, straight forward conversion rule implementation
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prv_sym = 'M'
        total = 0
        for sym in s:
            cur_num = table[sym]
            if table[prv_sym] < cur_num:
                cur_num -= table[prv_sym]
                total += cur_num - table[prv_sym]
            else:
                total += cur_num
            prv_sym = sym
        return total

# 98%, 124ms, adding all symbols and then subtract extra numbers from all 'smallBIG' combinations
class Solution:
    def romanToInt(self, s):
        return s.count("M")*1000 + s.count("D")*500 + s.count("C")*100 + s.count("L")*50 + \
            s.count("X")*10 + s.count("V")*5 + s.count("I")*1 - s.count("CD")*200 - \
            s.count("CM") * 200 - s.count("XL")*20 - s.count("XC")*20 - s.count("IV")*2 - \
            s.count("IX")*2
