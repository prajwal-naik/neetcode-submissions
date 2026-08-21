"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        N = len(intervals)
        if N == 0:
            return True
        intervals.sort(key = lambda x: x.start)
        for i in range(N):
            print(f"[{intervals[i].start}, {intervals[i].end}]")
        curEnd = intervals[0].end
        for i in range(1, N):
            newStart, newEnd = intervals[i].start, intervals[i].end
            if newStart < curEnd:
                return False
            curEnd = max(curEnd, newEnd)
        return True