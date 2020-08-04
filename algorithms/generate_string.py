class Solution:
    def generateTheString(self, n: int) -> str:
        result = ""

        if n % 2 == 0:
            inner_count = 1
            while inner_count < n:
                result += 'x'
                inner_count += 1
            result += 'y'
        else:
            inner_count = 1
            while inner_count <= n:
                result += 'x'
                inner_count += 1

        return result
