class Solution:
    def reverse(self, x: int) -> int:
        min_limit = (2 ** 31) * (-1)
        max_limit = (2 ** 31) - 1

        result = None
        
        if x >= min_limit and x <= max_limit:
            number = x

            if x < 0:
                number *= -1

            convertedNum = str(number)
            convertedNum = convertedNum[::-1]

            result = int(convertedNum)

            if x < 0:
                result *= -1
            if result < min_limit or result > max_limit:
                result = 0
        else:
            result = 0
            
        return result 
        