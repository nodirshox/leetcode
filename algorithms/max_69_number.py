class Solution:
    def maximum69Number (self, num: int) -> int:
        maxNum = num

        convertedNum = list(str(num))

        count = 0
        for digit in convertedNum:
            if int(digit) == 6:
                convertedNum[count] = 9
                newMax = ''
                for number in convertedNum:
                    newMax += str(number)
                if int(newMax) > maxNum:
                    maxNum = int(newMax)
                    break
            count += 1

        return maxNum