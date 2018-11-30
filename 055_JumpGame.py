# https://leetcode.com/problems/jump-game/

# 40ms 100%, time complexity O(n), space complexity O(1)
# 1. starting from the last index, find the largest index i that can reach it 
# 2. set target to i, starting from i, moving backward, find the largest index that can reach i
# 3. repeat till index 0, if target == 0, pass, otherwise, fail
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = len(nums) - 1
        for i in range(target - 1, -1, -1):
            if nums[i] + i >= target:
                target = i
        return target == 0
        
# greedy algorithm, iterating from index 0, keep updating maximum reach of each index
def canJump(self, nums):
    m = 0
    for i, n in enumerate(nums):
        if i > m:
            return False
        m = max(m, i+n)
    return True
