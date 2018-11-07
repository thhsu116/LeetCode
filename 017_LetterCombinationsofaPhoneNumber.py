# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# 100% 32ms, list comprehension for all combination, BFS
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        table = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        ret = table[digits[0]]
        try:
            for d in digits[1:]:
                ret = [s + c for s in ret for c in table[d]]
        except:
            pass
        return ret
        
# can also solve by DFS
