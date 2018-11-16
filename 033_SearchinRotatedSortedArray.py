# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

# 78% 40ms, two binary search
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        # first binary search to find index of the minimum number
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        rot = l
        
        nums = nums[rot:] + nums[:rot]  # rotate nums back
        # 2nd binary search to find target index
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return (mid + rot) % len(nums)
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        if nums[l] != target:
            return -1
        else:
            return (l + rot) % len(nums)
            
# one binary search
# https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple
