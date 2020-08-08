class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = []
        
        for num in A:
            result.append(num ** 2)
        
        result.sort()
        
        return result