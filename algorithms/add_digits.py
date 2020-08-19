class Solution:
    def addDigits(self, num: int) -> int:
        result = None
        is_found = False
        
        while is_found != True:
            converted_num = str(num)
            sum_of_digit = 0

            for digit in converted_num:
                sum_of_digit += int(digit)
            
            if sum_of_digit <= 9:
                is_found = True
                result = int(sum_of_digit)
            else:
                num = sum_of_digit
            
        return result