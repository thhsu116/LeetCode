# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# 52ms 89%, time complexity O(n), space complexity O(1)
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        prv = float('inf')
        for _ in range(len(nums)):
            cur = nums.pop(0)
            if cur == prv:
                cnt += 1
            else:
                cnt = 0
                prv = cur
            if cnt < 2:
                nums.append(cur)
                
 # 48ms 100%
 class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i
