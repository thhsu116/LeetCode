# https://leetcode.com/problems/subsets/

# 44ms 44%, iterative
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        for i in nums:
            ret += [r + [i] for r in ret]
        return ret

# DFS
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        
        def dfs(index, path):
            res.append(path)
            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]])

        dfs(0, [])
        return res
        
# python one liners
def subsets(self, nums):
    return reduce(lambda L, ele: L + [l + [ele] for l in L], nums, [[]])

def subsets(self, nums):
    [[x for x in l if x is not None] for l in itertools.product(*zip(nums, [None] * len(nums)))]

def subsets(self, nums):
    [l for n in range(len(nums) + 1) for l in itertools.combinations(nums, n)]
