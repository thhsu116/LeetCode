# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for i in range(len(nums)):
            num = nums[i]
            comp = target - num
            if num in table:
                return [table.get(num), i]
            table[comp] = i
