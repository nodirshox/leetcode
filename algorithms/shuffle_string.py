class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        converted = []

        count = 0
        while count < len(indices):
            converted.append('0')
            count += 1

        count_letter = 0
        while count_letter < len(indices):
            index_value = indices[count_letter]
            converted[index_value] = s[count_letter]

            count_letter += 1

        answer = ""

        count_string = 0
        while count_string < len(converted):
            answer += converted[count_string]
            count_string += 1

        return answer
