class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        
        for matrix in A:
            new_matrix = []
            for num in matrix:
                inner = []
                
                if num == 0:    
                    inner.append(1)
                else:
                    inner.append(0)
                    
                new_matrix = inner + new_matrix
                
            result.append(new_matrix)

        return result