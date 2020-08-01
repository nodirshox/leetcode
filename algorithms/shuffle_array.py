nums = [1,2,3,4,4,3,2,1]
result = []

lenght_of_nums = len(nums) / 2
counter = 0

while lenght_of_nums < len(nums):
    result.append(nums[counter])
    result.append(nums[int((lenght_of_nums - 1) + 1)])
    lenght_of_nums += 1
    counter += 1

print(nums)
print(result)