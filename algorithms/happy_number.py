class Solution:
    def isHappy(self, n: int) -> bool:
        is_happy = False

        is_equalls_to_one = False
        counter = 0
        while is_equalls_to_one == False:
            sum_of_squares = 0
            converted_number = str(n)

            for digit in converted_number:
                sum_of_squares += int(digit) ** 2
            #print(sum_of_squares)
            if sum_of_squares == 1:
                is_equalls_to_one = True
                is_happy = True
            else:
                n = sum_of_squares
            
            if counter == 1000:
                is_happy = False
                break
            
            counter += 1

        return is_happy
