'''Given a collection of intervals, merge all overlapping intervals'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # solution 1
        intervals.sort(key = lambda x: x.start)
        i = 0
        while i+1 < len(intervals):
            end = intervals[i].end
            if end >= intervals[i+1].start and end <= intervals[i+1].end:
                intervals[i].end = intervals[i+1].end
                del intervals[i+1]
            elif end > intervals[i+1].end:
                del intervals[i+1]
            else:
                i+=1
                
        return intervals
    
    
