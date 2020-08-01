nums = [3,7]
i = 0
j = 1

max_value = nums[i] * nums[j]

count = 0
for num in nums:
    second_count = 0
    for second_num in nums:
        if count != second_count:
            if num * second_num >= max_value:
                max_value = num * second_num
                i = count
                j = second_count
        second_count += 1
    count += 1

result = (nums[i] - 1) * (nums[j] - 1)
print(result)