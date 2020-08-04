left = 1
right = 22

arr = []
counter = left
while counter <= right:
    number = str(counter)
    is_self_dividing = True
    for digit in number:
        if int(digit) == 0:
            is_self_dividing = False
            continue
        if counter % int(digit) != 0:
            is_self_dividing = False
    if is_self_dividing:
        arr.append(counter)
    
    counter += 1

print(arr)