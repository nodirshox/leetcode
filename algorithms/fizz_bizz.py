class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        count = 1
        
        while count <= n:
            if count % 3 == 0 and count % 5 != 0:
                result.append("Fizz")
                count += 1
                continue
            elif count % 5 == 0 and count % 3 != 0:
                result.append('Buzz')
                count += 1
                continue
            elif count % 3 == 0 and count % 5 == 0:
                result.append('FizzBuzz')
            else:
                result.append(str(count))
            count += 1
        
        return result