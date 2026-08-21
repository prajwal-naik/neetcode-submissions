"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if intervals == []:
            return True

        intervals.sort(key = lambda x: x.end)

        currentStart = intervals[0].start
        currentEnd = intervals[0].end
        for interval in intervals[1:]:
            if (interval.start < currentStart) or (interval.start < currentEnd):
                return False
            else:
                currentStart = min(currentStart, interval.end)
                currentEnd = interval.end
        return True