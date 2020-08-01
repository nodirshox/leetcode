class Solution:
    def numberOfSteps (self, num: int) -> int:
        counter = 0

        while num >= 0:
            if num == 0:
                break
            if num > 0:
                if num % 2 == 0:
                    num = num / 2
                    counter += 1
                else:
                    num = num - 1
                    counter += 1

        return counter