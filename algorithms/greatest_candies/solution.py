class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        
        for candie in candies:
            selected = candie + extraCandies
            
            isBigger = True
            
            for otherCandies in candies:
                if selected < otherCandies:
                    isBigger = False
            
            result.append(isBigger)
            
        return result