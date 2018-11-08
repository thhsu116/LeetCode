# https://leetcode.com/problems/remove-element/description/

# 43% 48ms, two pointers and swap in place
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        min_val_idx = len(nums)
        for i in range(len(nums)):
            if i >= min_val_idx:
                break
            if nums[i] == val:
                j = min(min_val_idx, len(nums)-1)
                if i == j:
                    min_val_idx = j
                    break
                while j-i >= 0:
                    if nums[j] == val:
                        min_val_idx = j
                        j -= 1
                    else:
                        nums[i], nums[j] = nums[j], nums[i]
                        min_val_idx = j
                        break
        return min_val_idx
        
# two pointer approach 1 from solution
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
        
# two pointer approach#2 from solution
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        return n
