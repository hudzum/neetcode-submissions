"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
#Once sorted if start is within the prev interval conflict

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda interval: interval.start)
        for i in range(1, len(intervals)):
            if intervals[i-1].end > intervals[i].start:
                return False

        return True