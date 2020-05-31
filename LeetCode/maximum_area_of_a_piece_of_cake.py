
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        max_horizontal = 0
        max_vertical = 0
        for i in range(1, len(horizontalCuts)):
            if abs(horizontalCuts[i] - horizontalCuts[i-1]) > max_horizontal:
                max_horizontal = abs(horizontalCuts[i] - horizontalCuts[i-1])
                
        for i in range(1, len(verticalCuts)):
            if abs(verticalCuts[i] - verticalCuts[i-1]) > max_vertical:
                max_vertical = abs(verticalCuts[i] - verticalCuts[i-1])
                
                
        if max(horizontalCuts[0], h-horizontalCuts[-1]) > max_horizontal:
            max_horizontal = max(horizontalCuts[0], h-horizontalCuts[-1])

        if max(verticalCuts[0], w-verticalCuts[-1]) > max_vertical:
            max_vertical = max(verticalCuts[0], w-verticalCuts[-1])

            
        return (max_horizontal*max_vertical)%(10**9 + 7)
                
        
        
        
