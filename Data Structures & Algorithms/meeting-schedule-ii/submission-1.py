"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        current = 0
        end = sorted(intervals, key = lambda inter: inter.end)
        start = sorted(intervals, key = lambda inter: inter.start)
        i = 0
        j = 0
        while i < len(start):
            if start[i].start < end[j].end:
                current += 1
                i+=1
                res = max(current, res)
            else:
                current -= 1 
                j+=1

        return res

        #Sort both arrays start and end times
        #compare current start to current end 
        #if less than or equal next start & +1 concurrent
        #if greater than next end & -1 concurrent
