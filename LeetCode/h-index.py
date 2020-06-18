class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
           
        max_ = 0
        
        for i, citation in enumerate(sorted(citations)):
            if min(citation, len(citations) - i) > max_:
                max_ = min(citation, len(citations) - i)
        
        return max_
            
        
        
        
        
