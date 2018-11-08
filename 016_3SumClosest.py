# 85% 104ms, time complexity O(n^2), modify three pointers algorithm for 3sum to find combinaiton of a+b+c-target closet to 0
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = None
        min_diff = float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                diff = nums[i]+nums[l]+nums[r]-target
                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    ans = diff+target
                if diff > 0:
                    r -= 1
                elif diff < 0:
                    l +=1
                else:
                    return ans
        return ans
        
 
