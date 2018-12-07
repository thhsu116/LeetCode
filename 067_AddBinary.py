# https://leetcode.com/problems/add-binary/

# 48ms 71 %, time complexity O(n), space complexity O(n)
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = max(len(a), len(b))
        if len(a) < n:
            a = '0' * (n - len(a)) + a
        if len(b) < n:
            b = '0' * (n - len(b)) + b
        
        ret = ''
        co = 0
        for i in range(-1, -n-1, -1):
            s = (ord(a[i]) - 48 + ord(b[i]) - 48) + co
            num = s % 2 
            co = s // 2
            ret = chr(num + 48) + ret
        
        if co:
            return '1' + ret
        else:
            return ret
