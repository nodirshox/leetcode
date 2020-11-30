class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shufledArray = []
        counter = 0
        
        while counter < n:
            shufledArray.append(nums[counter])
            shufledArray.append(nums[counter + n])
            counter += 1
        
        return shufledArray