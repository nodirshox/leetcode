class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        result = []
        
        for num in A:
            if num % 2 == 0:
                result.append(num)

        for num in A:
            if num % 2 == 1:
                result.append(num)

        return result
        