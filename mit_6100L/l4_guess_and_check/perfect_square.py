## Guess and Check approach using exhaustive enumeration \
## to find out if a given positive integer is a perfect square

# Given n, value space for enumerations  to guess 0 to g , where g ** 2 <= n

num = int(input("Enter a positive integer: "))

for g in range(num):
    if g ** 2 == num:  # 
        print(num, "is a perfect square")
        break
    if g ** 2 > num:
        break

if g ** 2 != num:
    print(num, "is not a perfect square")


