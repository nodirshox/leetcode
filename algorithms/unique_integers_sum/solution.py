class Solution:
    def sumZero(self, n: int) -> List[int]:
        uniqueIntegers = []
        
        if n % 2 == 1:
            uniqueIntegers.append(0)
            n -= 1
        
        count = 1
        
        while count <= n / 2:
            uniqueIntegers.append((-1) * count)
            uniqueIntegers.append(count)
            count += 1
        
        return uniqueIntegers