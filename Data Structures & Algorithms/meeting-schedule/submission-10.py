"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        intervals.sort(key = lambda x : (x.start, -x.end))
        print(intervals)
        i = 1
        N = len(intervals)
        curEnd = intervals[0].end
        while i < N:
            newStart, newEnd = intervals[i].start, intervals[i].end
            if newStart < curEnd:
                return False
            else:
                curEnd = newEnd
            i += 1
        return True