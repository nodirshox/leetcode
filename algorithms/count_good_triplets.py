class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        result = 0
        
        i = 0
        for num in arr:
            j = 0
            for num2 in arr:
                k = 0
                for num3 in arr:
                    if 0 <= i and i < j and j < k and k < len(arr):
                        sub1 = arr[i] - arr[j]
                        sub2 = arr[j] - arr[k]
                        sub3 = arr[i] - arr[k]
                        if sub1 < 0:
                            sub1 *= -1
                        if sub2 < 0:
                            sub2 *= -1
                        if sub3 < 0:
                            sub3 *= -1
                        if sub1 <= a and sub2 <= b and sub3 <= c:
                            result += 1
                    k += 1
                j += 1
            i += 1

        return result
