# https://leetcode.com/problems/search-insert-position/description/

# 45% 44ms, binary search, time complexity O(logn)
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        elif target == nums[-1]:
            return len(nums)-1
        
        l = 0
        r = len(nums)-1
        while True:
            i = (r+l+1)//2
            if nums[i] == target:
                return i
            elif nums[i] > target:
                if nums[i-1] < target:
                    return i
                elif nums[i-1] == target:
                    return i-1
                r = i
            else:
                if nums[i+1] >= target:
                    return i+1
                l = i+1
                
# 99%, append, sort and then iterate
if target not in nums:
    nums.append(target)
for i, item in enumerate(sorted(nums)):
    if item == target:
        return i
