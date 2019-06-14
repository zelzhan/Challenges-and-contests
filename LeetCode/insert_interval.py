class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # (1, 2) (3, 10) (12, 16)
        # (3, 8)
        
        # [x] 1 interval
        
        if not intervals:
            return [newInterval]
        
        def is_overlap(a, b):
            return a[1] >= b[0] and b[1] >= a[0]
        
        def merge(a, b):
            return (min(a[0], b[0]), max(a[1], b[1]))
        
        i = 0
        start_inserting = False
        while i < len(intervals):
            if is_overlap(newInterval, intervals[i]):
                start_inserting = True
                newInterval = merge(newInterval, intervals[i])
                intervals.pop(i)
            elif start_inserting:
                intervals.insert(i, newInterval)
                start_inserting = False
                break
            elif not start_inserting and newInterval[1] < intervals[i][0]:
                intervals.insert(i, newInterval)
                break
            elif i == len(intervals)-1:
                intervals.append(newInterval)
                break
            else:
                i+=1
        
        if start_inserting:
            intervals.append(newInterval)
        return intervals
                
        
            
