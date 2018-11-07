# https://leetcode.com/problems/3sum/description/

# 89% 820ms, reduce to 2Sum problem, sort nums first so that duplicate answers will have elements in the same order
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def twoSum(_nums, target):
            sols = []
            table = {}
            for num in _nums:
                if num in table and [table[num], num] not in sols:
                    sols.append([table[num], num])
                else:
                    table[target-num] = num                    
            return sols
        
        nums.sort()  # sort first so that duplicate answers will have elements in the same order
        sols = []
        for i in range(len(nums)-2):
            num = nums[i]
            if i > 0 and num == nums[i-1]:
                continue
            sol = twoSum(nums[i+1:], 0-num)
            [s.append(num) for s in sol]
            sols += sol
        return sols

# iterate through all combinations and skip duplications, time complexity: O(n^2)
def threeSum(self, nums):
    res = []
    nums.sort()
    for i in xrange(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1 
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res
