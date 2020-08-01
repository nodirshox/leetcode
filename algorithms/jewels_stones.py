J = "z"
S = "ZZ"

count = 0

for letter in S:
    for another_letter in J:
        print(another_letter, 'vs', letter)
        if another_letter == letter:
            print('+1')
            count += 1

print(count)