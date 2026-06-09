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
        min_heap = []

        if len(intervals) == 1:
            return 1

        for i in range(len(intervals)):
            if min_heap and min_heap[0] <= intervals[i].start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, intervals[i].end)
        
        return 0 if len(intervals) == 0 else len(min_heap)
