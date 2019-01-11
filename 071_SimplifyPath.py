# https://leetcode.com/problems/simplify-path/

# 64ms, 96%, time O(n) space O(n)
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        split_path = path.split('/')
        ans = []
        for c in split_path:
            if c == '.':
                continue
            elif c == '..':
                if ans:
                    ans.pop()
            elif c:
                ans.append(c)
        if not ans:
            return '/'
        else:
            return '/'+'/'.join(ans)
            
# similar approach
class Solution(object):
    def simplifyPath(self, path):
        places = [p for p in path.split("/") if p!="." and p!=""]
        stack = []
        for p in places:
            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)
