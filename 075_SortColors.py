# https://leetcode.com/problems/sort-colors/

# 36ms 99%, one pass with swap
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos0 = 0
        pos2 = len(nums) - 1
        for i in range(len(nums)):
            while True:
                if nums[i] == 0 and i > pos0:
                    nums[i], nums[pos0] = nums[pos0],  nums[i]
                    pos0 += 1
                elif nums[i] == 2 and i < pos2:
                    nums[i], nums[pos2] = nums[pos2],  nums[i]
                    pos2 -= 1
                else:
                    break
                    
# one pass no swap
def sortColors(self, nums):
    i = j = 0
    for k in xrange(len(nums)):
        v = nums[k]
        nums[k] = 2
        if v < 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[i] = 0
            i += 1
