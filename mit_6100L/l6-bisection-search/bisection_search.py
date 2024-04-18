## Use Bisection search algorithm to find the square root of and  number

## use approximation to find a close enough square root of a given
## floating point number


num = float(input("Enter a floating point number"))
guess = 0
epsilon = 0.001


if num >= 1:
    low = 1.0
    high = num
else :
    low = num
    high = 1.0
guess = (low + high) / 2.0

n_guess = 1
while abs(guess ** 2 - num) >= epsilon:
    print(f'guesses : {n_guess}, low = {low}, high = {high}  guess = {guess}, number ={num} delta = {abs(guess ** 2 - num)}')
    if guess ** 2 > num:
        high = guess
    else:
        low = guess
    guess = (low + high)/2.0
    n_guess += 1
    
print(f'guesses : {n_guess},sqrt = {guess}, number ={num}')
    

