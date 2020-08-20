class Solution:
    def countOdds(self, low: int, high: int) -> int:
        differ = high - low
        
        if low % 2 == 1:
            differ += 1
        if high % 2 == 1:
            differ += 1
        
        return int(differ / 2)