class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        result = None
        length_of_array = len(A)
        
        for num in A:
            count = 0
            for number in A:
                if num == number:
                    count += 1
            
            if 2 * count == length_of_array:
                result = num
                break
        
        return result