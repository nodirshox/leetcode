class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        number = str(n)
        
        product_of_digits = 1
        sum_of_digits = 0
        
        for digit in number:
            product_of_digits *= int(digit)
            sum_of_digits += int(digit)
        
        result = product_of_digits - sum_of_digits
        
        return result
            