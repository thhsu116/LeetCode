# https://leetcode.com/problems/combination-sum/description/

# 96% 64ms, DFS with early termination
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, target, parent_idx, path, ans):
            if target == 0:
                ans.append(path)
                return
            for i in range(parent_idx, len(candidates)):
                if target-candidates[i] < 0:  # terminate DFS of this node since candidates is sorted
                    return
                dfs(candidates, target-candidates[i], i, path+[candidates[i]], ans)
                            
        candidates.sort()  # to enable early termination in DFS
        ans = []
        dfs(candidates, target, 0, [], ans)
        return ans
        
# back tracking
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        resList = []
        
        def backtracking(start, rest):
            if rest == 0:
                temp = resList[:]
                res.append(temp)
            for i in range(start, len(candidates)):
                if (candidates[i] <= rest):
                    resList.append(candidates[i])
                    backtracking(i, rest-candidates[i])
                    resList.pop()
            
        backtracking(0, target)
        return res
