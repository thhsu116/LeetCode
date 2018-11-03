# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# 18%, 448ms, sliding window, recreate lookup table when duplication is detected
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = {}
        ans = 0
        for i in range(len(s)):
            c = s[i]
            if c not in chars:
                chars[c] = i
            else:
                ans = max(len(chars), ans)
                c_idx = chars[c]
                chars = {}
                for j in range(c_idx+1, i+1):
                    chars[s[j]] = j
        return max(ans, len(chars))
        
# 76%, 92ms, sliding window, remove characters before the left duplicant from lookup table when duplication is detected
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = {}
        start = 0
        ans = 0
        for i in range(len(s)):
            c = s[i]
            if c not in chars:
                chars[c] = i
            else:
                ans = max(len(chars), ans)
                c_idx = chars[c]
                for j in range(start, c_idx+1):
                    del chars[s[j]]
                start = c_idx+1
                chars[c] = i
        return max(ans, len(chars))
