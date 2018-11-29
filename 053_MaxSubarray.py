# https://leetcode.com/problems/maximum-subarray

# 44ms 98%, time complexity O(n)
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = float('-inf')
        sm = 0
        for n in nums:
            sm = max(sm + n, n)
            if sm > mx:
                mx = sm
        return mx
