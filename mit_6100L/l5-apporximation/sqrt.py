## use approximation to find a close enough square root of a given
## floating point number


num = float(input("Enter a floating point number"))
guess = 0
epsilon = 0.01
increment = 0.001

n_guess = 1
while abs(guess ** 2 - num) > epsilon and guess ** 2 < num:
    print(f'guesses : {n_guess}, delta = {abs(guess ** 2 - num)},  guess = {guess}, number ={num}')
    guess += increment
    n_guess += 1
    if n_guess % 10000 == 0 :
        input("continue")


