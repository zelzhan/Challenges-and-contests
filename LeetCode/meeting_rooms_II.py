class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        starts, ends = [], []

        for s, e in intervals:
            starts.append(s)
            ends.append(e)


        res = 0

        conc = 0

        i, j = 0, 0
        starts.sort()
        ends.sort()
        

        while i < len(intervals) and j < len(intervals):
            if starts[i] < ends[j]:
                if conc > res:
                    res = conc
                conc+=1
                i+=1

            elif starts[i] > ends[j]:
                conc-=1
                j+=1
            else:
                i+=1
                j+=1


        return res+1
