nums = [1,2,3]
result = 0

i = 0
for num in nums:
    j = 0
    for another_num in nums:
        if i != j and nums[i] == nums [j] and i < j:
            result += 1
        
        j += 1
    
    i += 1

print(result)