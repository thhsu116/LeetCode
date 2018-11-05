# https://leetcode.com/problems/longest-palindromic-substring/description/

# 44%, 1956ms, iterate through each character in s as center, sapn left and right to check for palindrome
# time complexity O(n^2), space complexity O(1)
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ''
        for i in range(len(s)):
            span = min(i, len(s)-i-1)
            if len(ret) >= 2*span + 1:
                break
            palindrome = s[i]
            step = 1
            while span > 0 and step <= span:
                if s[i - step] == s[i + step]:
                    palindrome = s[i - step] + palindrome + s[i + step]
                    step += 1
                else:
                    break
            if len(ret) < len(palindrome):
                ret = palindrome
                
            if i <= len(s)-2 and s[i] == s[i+1]:
                span = min(i, len(s)-i-2)
                palindrome = s[i] + s[i+1]
                step = 1
                while span > 0 and step <= span:
                    if s[i - step] == s[i + 1 + step]:
                        palindrome = s[i - step] + palindrome + s[i + 1 + step]
                        step += 1
                    else:
                        break
                if len(ret) < len(palindrome):
                    ret = palindrome
        return ret
      
# Manacher's Algorithm, time complexity O(n), space complexity O(n)
# https://articles.leetcode.com/longest-palindromic-substring-part-ii/
