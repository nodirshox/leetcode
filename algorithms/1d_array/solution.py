class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        sumNumber = []
        for number in nums:
            sum += number
            sumNumber.append(sum)
        
        return sumNumber