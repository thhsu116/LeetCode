# https://leetcode.com/problems/merge-intervals/

# 56ms 100%, first sort intervals based on start values, then interate through invervals and perfrom merge
# time complexity O(nlogn), space complexity O(n)
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
        
        intervals.sort(key=lambda x: x.start)
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            s = intervals[i].start
            e = intervals[i].end
            if s <= res[-1].end:
                if e > res[-1].end:
                    res[-1].end = e
            else:
                res.append(intervals[i])
        return res
