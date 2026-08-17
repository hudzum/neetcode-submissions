"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        concurrent = 0
        res = 0
        i = 0
        j = 0
        while i < len(start):
            if start[i] < end[j]:
                concurrent += 1
                i+=1
            elif start[i] >= end[j]:
                concurrent -= 1
                j+=1
            res = max(concurrent, res)
        return res
        # [0, 5, 15]
        # [40, 10, 20]
        #compare current start and next start