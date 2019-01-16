# https://leetcode.com/problems/subsets-ii/

# 64ms 99%, save new subsets from each iteration
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()        
        ans = [[]]
        prv = float('INF')
        prv_new = []
        for i in nums:
            if i != prv:
                new = [a + [i] for a in ans]
            else:
                new = [a + [i] for a in prv_new]
            ans += new
            prv = i
            prv_new = new
        return ans

# 68ms 85%, save index of the first new subset in ans from each iteration
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()        
        ans = [[]]
        prv = float('INF')
        for i in nums:
            prv_len = len(ans)
            if i != prv:
                ans += [a + [i] for a in ans]
            else:
                ans += [a + [i] for a in ans[idx:]]
            prv = i
            idx = prv_len
        return ans
