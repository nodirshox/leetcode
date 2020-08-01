class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []

        i = 0
        for num in nums:
            j = 0
            count = 0
            for another_num in nums:
                if i != j:
                    if num > another_num:
                        count += 1
                j += 1

            result.append(count)
            i += 1

        return result