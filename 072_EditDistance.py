# https://leetcode.com/problems/edit-distance/

# 284 ms 83%, DP, time O(mn), space O(n)
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        d_list = list(range(len(word2) + 1))
        l1 = len(word1)
        l2 = len(word2)
        #print(d)
        for i in range(1, l1+1):
            d = i
            for j in range(1, l2+1):
                left = d
                down = d_list[j]
                down_left = d_list[j-1]
                if word1[i-1] == word2[j-1]:
                    down_left -= 1
                d = 1 + min([left, down, down_left])
                d_list[j-1] = left
            d_list[-1] = d
            #print(d)
        return d_list[-1]
