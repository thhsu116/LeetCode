# https://leetcode.com/problems/zigzag-conversion/description/

# 58%, 112ms, by calaulating relative position between each character in the answer, Visit by Row algorithm in solution
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        length = len(s)
        ret = ''
        step = numRows - 2 + numRows
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                col = i
                while col < length:
                    ret += s[col]
                    col += step
            else:
                col = i
                while col < length:
                    slash = col + step - 2*i
                    if slash < length:
                        ret += s[col] + s[slash]
                    else:
                        ret += s[col]
                    col += step
                
        return ret

# 61%, 108ms, Sort by Row algorithm in solution
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        pattern = {}
        row = 0
        step = 1 # 1: down, -1 up-left
        for c in s:
            if row not in pattern:
                pattern[row] = c
            else:
                pattern[row] += c
            row += step
            if row == 0 or row == numRows-1:
                step *= -1
        ret = ''
        for i in range(numRows):
            try:
                ret += pattern[i]
            except:
                return ret            
        return ret
        
