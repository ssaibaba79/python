
is_negative = False
num = int(input("Enter a integer number"))

if num < 0:
    is_negative = True
    num = abs(num)

binary = ''

if num == 0:
    binary += '0'
else:
    while num > 0:
        binary = str(num % 2) + binary
        num = num //2

if is_negative:
    binary += '-' + binary

print(binary)