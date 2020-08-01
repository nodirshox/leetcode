class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0

        for letter in S:
            for another_letter in J:
                if another_letter == letter:
                    count += 1

        return count
