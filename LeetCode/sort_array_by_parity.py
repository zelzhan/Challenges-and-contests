class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        i = j = 0
        while i < len(A):
            
            while i < len(A) and A[i]%2 == 0:
                i+=1
                
            if i == len(A):
                break
            
            j = i
            
            while j < len(A) and A[j]%2 !=0:
                j+=1
            
            if j == len(A):
                break
            
            A[j], A[i] = A[i], A[j]
            
            
        return A
            
