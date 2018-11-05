# https://leetcode.com/problems/valid-parentheses/description/

# 9% 64ms, continuous split
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s) % 2:
            return False
        
        while s:
            s_split = s.split('()')
            if len(s_split) > 1:
                s = ''.join(s_split)
                continue
            s_split = s.split('[]')
            if len(s_split) > 1:
                s = ''.join(s_split)
                continue
            s_split = s.split('{}')
            if len(s_split) > 1:
                s = ''.join(s_split)
                continue
            else:
                return False
        return True
