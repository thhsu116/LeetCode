# https://leetcode.com/problems/longest-common-prefix/description/

# 82%, 40ms
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ''
        i = 0
        while True:
            try:
                chars = [s[i] for s in strs]
                c_ref = chars.pop()
                if all(c == c_ref for c in chars):
                    ans += c_ref
                else:
                    break
            except:
                break
            i += 1
        return ans
        
# 36ms, use zip to iterate through each character of all strings 
def longestCommonPrefix(strs):
        res = ''
        flag = False
        
        for x in zip(*strs):
            if flag: break
            first = x[0]
            for c in x[1:]:
                if c != first:
                    flag = True
                    break
            res += first if not flag else '' 
            
        return res
