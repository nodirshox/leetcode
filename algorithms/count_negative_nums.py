class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        
        for matrix in grid:
            for element in matrix:
                if element < 0:
                    result += 1
        
        return result