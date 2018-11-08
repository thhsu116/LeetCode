# https://leetcode.com/problems/4sum/description/

# 97% 88ms, reduce to 3 sum problem, 22% wihtout early termination
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def threeSum(_nums, _target):
            ret = []
            for i in range(len(_nums)-2):
                if _target < _nums[i]*3 or _target > _nums[-1]*3:  # early termination by taking advantage of sort
                    break
                l = i+1
                r = len(_nums)-1
                while l < r:
                    _sum = _nums[i] + _nums[l] + _nums[r]
                    if _sum == _target:
                        ret.append([_nums[i], _nums[l], _nums[r]])
                        l += 1
                        r -= 1
                    elif _sum > _target:
                        r -= 1
                    else:
                        l += 1
            return ret
                    
        ans = []
        nums.sort()
        for i in range(len(nums)-3):
            if target < nums[i]*4 or target > nums[-1]*4:  # # early termination by taking advantage of sort
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            three_sum = threeSum(nums[i+1:], target-nums[i])
            if three_sum:
                for ts in three_sum:
                    ts.append(nums[i])
                    if not ts in ans:
                        ans.append(ts)
        return ans
        
# recursive
def fourSum(self, nums, target):
    def findNsum(l, r, target, N, result, results):
        if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  # early termination
            return
        if N == 2: # two pointers solve sorted 2-sum problem
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else: # recursively reduce N
            for i in range(l, r+1):
                if i == l or (i > l and nums[i-1] != nums[i]):
                    findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

    nums.sort()
    results = []
    findNsum(0, len(nums)-1, target, 4, [], results)
    return results
