# https://leetcode.com/problems/minimum-window-substring/

# 248ms 47%, time O(n), space O(1)(up to number of ASCII characters)
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter

        hash_map = Counter(t)
        res = ''
        left = 0
        cnt = 0
        minlen = float('INF')

        for i in range(len(s)):
            if s[i] in hash_map:
                hash_map[s[i]] -= 1
                if hash_map[s[i]] >= 0:
                    cnt += 1
            while cnt == len(t):
                if minlen > i - left + 1:
                    minlen = i - left + 1
                    res = s[left: i + 1]
                if s[left] in hash_map:
                    hash_map[s[left]] += 1
                    if hash_map[s[left]] > 0:
                        cnt -= 1
                left += 1

        return res
        
# use list, instead of dict to count letters in t
# 176ms 80%, time O(n), space O(1)
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letter_cnt = [0] * 128  # upto 128 alphabet characters
        for c in t:
            letter_cnt[ord(c)] += 1
        res = ''
        left = 0
        cnt = 0
        minlen = float('INF')

        for i in range(len(s)):
            if s[i] in t:
                letter_cnt[ord(s[i])] -= 1
                if letter_cnt[ord(s[i])] >= 0:
                    cnt += 1
            while cnt == len(t):
                if minlen > i - left + 1:
                    minlen = i - left + 1
                    res = s[left: i + 1]
                if s[left] in t:
                    letter_cnt[ord(s[left])] += 1
                    if letter_cnt[ord(s[left])] > 0:
                        cnt -= 1
                left += 1

        return res
