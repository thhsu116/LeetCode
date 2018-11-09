# https://leetcode.com/problems/generate-parentheses/description/

# 99% 36ms, recursive similar to approach 2 in solution, time and sapce complexity O(4^n/sqrt(n))
# complexity analysis: https://leetcode.windliang.cc/leetCode-22-Generate-Parentheses.html?q=
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ANS = []
        
        def popParenthesis(head, lp, rp):
            if not lp:
                ANS.append(head+')'*len(rp))
                return
            
            if len(lp) == len(rp):
                popParenthesis(head+'(', lp[:-1], rp)
            elif len(lp) < len(rp):
                popParenthesis(head+'(', lp[:-1], rp)
                popParenthesis(head+')', lp, rp[:-1])
            else:
                raise Exception('should not happen')
        
        popParenthesis('', ['(']*n, [')']*n)
        return ANS

# approach 3 in solution, spliting valid sequences to the form of ("lef valid seq")"right valid seq"
# time and space complexity is the same as approach 2
class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in xrange(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
