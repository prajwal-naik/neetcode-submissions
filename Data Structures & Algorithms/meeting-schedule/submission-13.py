"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        N = len(intervals)
        if N == 0:
            return True
        curEnd = intervals[0].end

        for i in range(1, N):
            s, e = intervals[i].start, intervals[i].end
            if s < curEnd:
                return False
            curEnd = e
        return True