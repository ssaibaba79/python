import random

# random number between 0 - 1
for i in range(10):
    r = random.random()
    print(r)

# random value withing provided min/max limits
x = random.randint(5, 10)
print(x)

# pick random value based on provided choices
options = ["SIMPLE","MEDIUM","COMPLEX"]
print(random.choice(options))
