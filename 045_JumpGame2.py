# https://leetcode.com/problems/jump-game-ii/

# greedy, time compexity O(n), space complexity O(1)
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        current_jump_max = 0
        previous_jump_max = 0
               
        for i in range(len(nums) - 1):
            current_jump_max = max(current_jump_max, i + nums[i])
            #Note 1         
            if i == previous_jump_max:
                jumps += 1 
                previous_jump_max = current_jump_max
                #Note 2            
        return jumps
        
# DP, from last to first, calculate min steps required to last
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] >= n:
            return 1
        min_steps = [0] * n  # minimum steps to end of every index in nums
        for i in range(n-2, -1, -1):
            if nums[i] == 0:
                min_steps[i] = float('inf')
                continue
            min_steps[i] = 1 + min(min_steps[i+1: min(i+nums[i]+1, n)])
        #print(min_steps)
        return min_steps[0]
        
# O(n), BFS
# https://leetcode.com/problems/jump-game-ii/discuss/18028/O(n)-BFS-solution
class Solution:
    def jump(self, nums):
        """
        Greedy implementation maximizing the length of each jump.
        :type nums: List[int]
        :rtype: int
        """
        current_index = 0
        target_index = len(nums) - 1 
        total_jumps = 0
        
        while current_index < target_index:
            total_jumps += 1
            jump_range = range(current_index, current_index + nums[current_index] + 1) 
            if target_index in jump_range:
                break
                
            next_index = current_index
            for next_index_candidate in jump_range:               
                candidate_jump_destination = next_index_candidate + nums[next_index_candidate]
                next_jump_destination = next_index + nums[next_index]
                if next_jump_destination < candidate_jump_destination :
                    next_index = next_index_candidate

            current_index = next_index

        return total_jumps
