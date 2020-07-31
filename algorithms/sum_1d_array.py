nums = [1, 2, 3, 4]
answer = []
for numbers in nums:
    try:
        sum_of_numbers = answer[-1] + numbers
    except:
        sum_of_numbers = numbers
    answer.append(sum_of_numbers)

print(answer)