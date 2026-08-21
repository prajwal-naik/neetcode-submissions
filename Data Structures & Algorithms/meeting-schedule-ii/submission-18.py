"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        intervals.sort(key = lambda x: x.start)
        res = 0
        for interval in intervals:
            start, end = interval.start, interval.end
            if heap:
                earliestEnd = heap[0][0]
                if earliestEnd <= start:
                    heapq.heappop(heap)
            heapq.heappush(heap, (end, start))
            res = max(res, len(heap))
        return res