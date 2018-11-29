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

    # divide and conquer
    # http://www.cnblogs.com/grandyang/p/4377150.html
    class Solution:
    def maxSub(self, nums, l, r):
        if l > r:
            return float('-inf')
        
        m = int(l + (r-l)/2)
        lmax = self.maxSub(nums, 0, m-1)
        rmax = self.maxSub(nums, m+1, r)

        ml, mr = 0, 0
        sm = 0
        for i in range(m-1, l-1, -1):
            sm += nums[i]
            ml = max(ml, sm)

        sm = 0
        for i in range(m+1, r+1):
            sm += nums[i]
            mr = max(mr, sm)

        return max(max(lmax, rmax), ml + mr + nums[m])
    
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        return self.maxSub(nums, 0, len(nums)-1)
