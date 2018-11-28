# https://leetcode.com/problems/first-missing-positive/

# 48ms, 38%, time complexity O(n), space complexity O(n)
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        mx = max(nums)
        s_nums = set(nums)
        for i in range(1, mx+1):
            if i not in s_nums:
                return i
        return mx+1
        
 # 52ms 26%, time complexity O(n)?
 class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        ret = 1
        n = len(nums)
        cnt = 0
        while True:
            cnt += 1
            num = nums.pop(0)
            if num == ret:
                cnt = 0
                n -= 1
                ret += 1
            else:
                nums.append(num)
            if cnt == n:
                return ret
                
# 48ms 38%, time complexity O(n), space complexity O(1)
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i <= len(nums):
            x = nums[i-1]
            if 1 <= x <= len(nums) and nums[x-1] != x:
                nums[i-1], nums[x-1] = nums[x-1], x
            else:
                i += 1
        for i, x in enumerate(nums, 1):
            if i != x:
                return i
        return len(nums)+1
