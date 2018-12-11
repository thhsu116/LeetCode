# https://leetcode.com/problems/valid-number/

# 72ms 57%
class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def pre_e(string):
            if not string:
                return False
            if string[0] == '+' or string[0] == '-':
                string = string[1:]
            if not string:
                return False
            if '.' in string:
                string_split = string.split('.')
                if len(string_split) == 2 and (string_split[0] or string_split[1]):
                    return all(s.isdigit() for s in string_split[0]) and all(s.isdigit() for s in string_split[1])
                else:
                    return False
            else:
                return all(s.isdigit() for s in string)
        
        def post_e(string):
            if not string:
                return False
            if string[0] == '+' or string[0] == '-':
                string = string[1:]
            if string:
                return all(s.isdigit() for s in string)
            else:
                return False
        
        s = s.strip()
        if 'e' in s:
            s_split = s.split('e')
            if len(s_split) == 2:
                return pre_e(s_split[0]) and post_e(s_split[1])
            else:
                return False
        else:
            return pre_e(s)
            
# regular expression
class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        return bool(re.match('^[+-]?(\d+\.?|\.\d+)\d*(e[+-]?\d+)?$', s.strip()))
