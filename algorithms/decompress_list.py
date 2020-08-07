class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:

        result = []
        count = 0

        while count < len(nums):
            freq = nums[count]
            val = nums[count + 1]
            inner_count = 0
            while inner_count < freq:
                result.append(val)
                inner_count += 1
            count += 2

        return result