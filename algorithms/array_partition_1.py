class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        count = 0
        
        while count < len(nums):
            result += nums[count]
            count += 2
        
        return result