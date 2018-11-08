# https://leetcode.com/problems/implement-strstr/description/

# 96% 36ms, ues split(), time complexity O(n), space complexity O(n)
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        splited = haystack.split(needle)
        if len(splited) == 1:
            return -1
        else:
            return len(splited[0])
            

# linear search, time complexity O(n), space complexity O(1)
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l1 = len(haystack)
        l2 = len(needle)
        
        if l2 == 0:
            return 0
        for i in range(len(haystack)):
            if i + l2 <= l1 and haystack[i:i+l2] == needle:
                    return i
            else:
                continue
        return -1 
