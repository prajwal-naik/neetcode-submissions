"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        currentMeetings = []
        res = 0
        for interval in intervals:
            if currentMeetings and currentMeetings[0] <= interval.start:
                heapq.heappop(currentMeetings)
            heapq.heappush(currentMeetings, interval.end)
            res = max(res, len(currentMeetings))
        return res