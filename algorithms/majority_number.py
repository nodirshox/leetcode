class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = None
        checked_nums = []
        count = 0
        while count < len(nums):
            selected_number = nums[count]
            if selected_number not in checked_nums:
                appears = 1
                inner_count = 0
                while inner_count < len(nums):
                    if count != inner_count:
                        if selected_number == nums[inner_count]:
                            appears += 1

                    inner_count += 1

                if appears > len(nums) / 2:
                    result = selected_number
                    break
            checked_nums.append(selected_number)
            count += 1
        
        return result