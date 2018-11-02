# https://leetcode.com/problems/string-to-integer-atoi/description/

# using python string method isdigit()
class Solution:
    def myAtoi(self, _str):
        """
        :type _str: str
        :rtype: int
        """
        num_str = ""
        str_strip = _str.strip()
        if not str_strip:
            return 0
        sign = '+'
        if str_strip[0] in ['-', '+']:
            sign = str_strip[0]
            str_strip = str_strip[1:]
        
        ret = ""
        for s in str_strip:
            if s.isdigit():
                ret += s  # ret = ret*10 + ord(s) - ord('0') if str to int is prohibited
            else:
                break
        if ret:
            if sign == '-':
                ret = -1*int(ret)
            else:
                ret = int(ret)
            if ret > 2147483647:
                return 2147483647
            elif ret < -2147483648:
                return -2147483648
            else:
                return ret
        else:
            return 0
