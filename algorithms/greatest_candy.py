candies = [12,1,12]
extraCandies = 10

result = []

for candy in candies:
    sum_candy = candy + extraCandies
    answer = True
    for another_candy in candies:
        if sum_candy < another_candy:
            answer = False
    result.append(answer)

print(result)