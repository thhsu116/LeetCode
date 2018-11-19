# https://leetcode.com/problems/permutations/

# 85% 52ms, recursive
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permute_list(num_list):
            if len(num_list) <= 1:
                return [num_list]
            elif len(num_list) == 2:
                return [num_list, [num_list[1], num_list[0]]]
            else:
                ret = []
                for i in range(len(num_list)):
                    ret += [[num_list[i]]+l for l in permute_list(num_list[0:i]+num_list[i+1:])]
                return ret

        return permute_list(nums)

# 85% 52ms, DFS
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ANS = []
        def dfs(nums, path):
            if not nums:
                ANS.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[0:i]+nums[i+1:], path + [nums[i]])
        dfs(nums, [])
        return ANS
