# https://leetcode.com/problems/length-of-last-word/

# 32ms 100%, search Word from the last index
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        s = s.rstrip()
        if not s:
            return 0
        for i in range(len(s)-1, -1, -1):
            if s[i].isalpha():
                res += 1
            else:
                return res
        return res
