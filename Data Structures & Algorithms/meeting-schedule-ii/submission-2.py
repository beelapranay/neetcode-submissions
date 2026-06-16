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
        res = 0
        min_heap = []

        for i in range(len(intervals)):
            if min_heap:
                if min_heap[0] <= intervals[i].start:
                    heapq.heappop(min_heap)
            heapq.heappush(min_heap, intervals[i].end)
            res += 1
        
        return len(min_heap)

        #TC: O(n log n)
        #SC: O(n)
