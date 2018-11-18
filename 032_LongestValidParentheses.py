#

# 60ms 65%, iterate over s, save left parentheses's index to a stack
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        start = i
        l_left = []
        ans = 0
        while i < len(s):
            if s[i] == ')':
                if len(l_left) == 0:
                    start = i+1
                else:
                    l_left.pop()
                    if len(l_left) == 0:
                        ans = max(ans, i-start+1)
                    else:
                        ans = max(ans, i-l_left[-1])
            else:
                l_left.append(i)
            i += 1
        return ans
        
 # DP https://leetcode.com/problems/longest-valid-parentheses/discuss/14133/My-DP-O(n)-solution-without-using-stack
 # DP http://bangbingsyb.blogspot.com/2014/11/leetcode-longest-valid-parentheses.html
