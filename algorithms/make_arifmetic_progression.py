arr = [3, 5, 1]
arr.sort()

sub = arr[1] - arr[0]

counter = 0
is_progression = True
for num in arr:
    if counter != len(arr) - 1:
        if arr[counter + 1] - arr[counter] != sub:
            is_progression = False
            break
    counter += 1

print(is_progression)


