class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            converted = str(num)
            sum_digits = 0
            
            for digit in converted:
                print(sum_digits)
                sum_digits += int(digit)
            
            if sum_digits < 10:
                return int(sum_digits)
            
            num = int(sum_digits)