class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        count = 1
        len_of_arr = n
        
        if n % 2 == 1:
            answer.append(0)
            leng_of_arr = n-1

        while count <= len_of_arr / 2:
            answer.append(count)
            answer.append(count * (-1))
            count += 1

        return answer