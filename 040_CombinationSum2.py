# https://leetcode.com/problems/combination-sum-ii/description/

# 100% 48ms, sort then DFS recursion with removing parent node from candidates
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ANS = []
        def dfs(nums, target, start, path):
            if start >= len(nums):
                return
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                if nums[i] == target:
                    ANS.append(path + [nums[i]])
                    return
                elif nums[i] > target:
                    return
                dfs(nums, target - nums[i], i+1, path + [nums[i]])
        
        candidates.sort()
        dfs(candidates, target, 0, [])
        return ANS
        
# dynamic programing
def combinationSum2(self, candidates, target):
    candidates.sort()
    table = [None] + [set() for i in range(target)]
    for i in candidates:
        if i > target:
            break
        for j in range(target - i, 0, -1):
            table[i + j] |= {elt + (i,) for elt in table[j]}
        table[i].add((i,))
    return map(list, table[target])
