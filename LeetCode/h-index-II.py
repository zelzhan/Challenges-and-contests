class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations) - 1
        if not citations:
            return 0
    
    
        while left < right:
            mid = left + (right-left)//2
            
            if citations[mid] > len(citations) - mid:
                right = mid
            elif citations[mid] < len(citations) - mid:
                left = mid + 1
            else:
                return citations[mid]
            
        
        return min(citations[right], len(citations) - right)
