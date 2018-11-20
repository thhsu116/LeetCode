# https://leetcode.com/problems/group-anagrams/

# 56% 140ms, sort individual str alphabetically, then use dictionary to look up
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def encoder(s):
            uni_int = [ord(c) for c in s]
            uni_int.sort()
            return ''.join(chr(ui) for ui in uni_int)
        
        ans = {}
        for s in strs:
            enc_s = encoder(s)
            if enc_s in ans:
                ans[enc_s].append(s)
            else:
                ans[enc_s] = [s]
                
        return list(ans.values())
        
# 99% 116ms, use sorted() to sort individual str alphabetically, convert to tuple to save as key for look up
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """        
        ans = {}
        for s in strs:
            enc_s = tuple(sorted(s))
            if enc_s in ans:
                ans[enc_s].append(s)
            else:
                ans[enc_s] = [s]
                
        return list(ans.values())
