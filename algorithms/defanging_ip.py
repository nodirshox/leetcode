address = '255.100.50.0'

new_address = ''

for digit in address:
    if digit == '.':
        new_address += '[.]'
    else:
        new_address += str(digit)

print(new_address)