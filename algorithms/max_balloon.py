class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b_val = 0
        a_val = 0
        l_val = 0
        o_val = 0
        n_val = 0

        count = 0
        while count < len(text):
            letter = text[count]
            if letter == 'b':
                b_val += 1
            elif letter == 'a':
                a_val += 1
            elif letter == 'l':
                l_val += 1
            elif letter == 'o':
                o_val += 1
            elif letter == 'n':
                n_val += 1

            count += 1

        result = 0
        counter = 0
        while counter < len(text) / 7:
            """
            1 - b; 1 - a; 2 - l; 2 - o; 1 - n
            """
            if b_val >= 1 and a_val >= 1 and l_val >= 2 and o_val >= 2 and n_val >= 1:
                result += 1
                b_val -= 1
                a_val -= 1
                l_val -= 2
                o_val -= 2
                n_val -= 1
            counter += 1

        return result

