# https://leetcode.com/problems/permutation-sequence/

# 40ms 81%, time complexity O(n), space complexity O(n)
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from math import factorial
        nums = list(map(str, range(1, n+1)))
        res = ''
        while k >= 1:
            if k == 1:
                return res + ''.join(nums)
            n1f = factorial(n-1)
            res += nums.pop((k-1) // n1f)
            n -= 1
            k -= (k-1) // n1f * n1f
