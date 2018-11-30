# https://leetcode.com/problems/insert-interval/

# 60ms 78%, time complexity O(n), space complexity O(n)
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        res = []
        for i in range(len(intervals)):
            intv = intervals[i]
            if intv.end < newInterval.start:
                res.append(intv)
            elif intv.start > newInterval.end:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval.start = min(intv.start, newInterval.start)
                newInterval.end = max(intv.end, newInterval.end)
        return res + [newInterval]
