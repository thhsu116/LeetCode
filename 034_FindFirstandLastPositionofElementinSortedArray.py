# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

# 8% 68ms, use Counter, not O(logn)
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        from collections import Counter
        
        counter = Counter(nums)
        if target in counter:
            s, e = 0, 0
            key = list(counter.keys())
            key.sort()
            for num in key:  # assuming sorted
                if num < target:
                    s += counter[num]
                elif num == target:
                    e = s + counter[num] - 1
                    return [s, e]
        else:
            return [-1, -1]
            
# 93% 40ms, use intertools.groupby(), since nums is already sorted
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        import itertools
        
        s = 0
        for num, group in itertools.groupby(nums):
            if num < target:
                s += len(list(group))
            elif num == target:
                return [s, s + len(list(group)) -1]
            elif num > target:
                return [-1, -1]
        return [-1, -1]  # for null test
        
# binary search solution for O(logn) time complexity
class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]
