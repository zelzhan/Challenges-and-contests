class RecentCounter:    
    def __init__(self):
        self.timings = []
        

    def ping(self, t: int) -> int:
        self.timings.append(t)
        i = len(self.timings) - 2
        
        counter = 1
        while i >= 0 and self.timings[i] >= t - 3000:
            i-=1
            counter+=1
        
        return counter
