# https://leetcode.com/problems/combinations/

# 136ms 89%, DFS recursive
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def comb(nums, k):
            if k == len(nums):
                return [nums]
            elif k == 1:
                return [[n] for n in nums]
            res = []
            for i in range(len(nums) - k + 1):
                res += [[nums[i]] + p for p in comb(nums[i+1:] , k - 1)]
            return res

        return comb(list(range(1, n + 1)), k)
        

# https://leetcode.com/problems/combinations/discuss/27024/1-liner-3-liner-4-liner
# Library - AC in 64 ms
from itertools import combinations
class Solution:
    def combine(self, n, k):
        return list(combinations(range(1, n+1), k))
        

# Recursive - AC in 76 ms
class Solution:
    def combine(self, n, k):
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]
        
# Reduce - AC in 76 ms
class Solution:
  def combine(self, n, k):
    return reduce(lambda C, _: [[i]+c for c in C for i in range(1, c[0] if c else n+1)],
                  range(k), [[]])
