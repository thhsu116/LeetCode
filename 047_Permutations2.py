# https://leetcode.com/problems/permutations-ii/

# 73% 76ms, DFS with check of numbers called for DFS
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ANS = []
        def dfs(nums, path):
            if not nums:
                ANS.append(path)
                return
            visited = set()
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                else:
                    visited.add(nums[i])
                dfs(nums[0:i]+nums[i+1:], path + [nums[i]])
        dfs(nums, [])
        return ANS
        
