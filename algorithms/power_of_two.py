class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        result = False
        
        if n > 0:
            if n == 1:
                result = True
            else:
                while n > 1:
                    if n % 2 == 0:
                        n = n / 2
                        result = True
                    else:
                        result = False
                        break

        return result