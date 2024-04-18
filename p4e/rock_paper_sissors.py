
from random import randint
from time import sleep

print("Lets play Rock, Paper, Sisscors")
print("type Rock, Paper or Sisscors to pick one and press enter")



while True:
    options = ["ROCK","PAPER","SISSCORS"]
    
    for option in options:
        print(option)
        sleep(1)

    users_pick =  input("You Shoot:")
    computer_pick = options[randint(0,2)]
    
    winner = None
    
    if users_pick:
        users_pick = users_pick.upper()
        print("You picked:"+ users_pick )
        print("I picked :" + computer_pick)
        
        if users_pick == computer_pick:
            winner = "No one"
        elif users_pick == "ROCK" and computer_pick == "SISSCORS":
            winner ="You"
        elif users_pick == "SISSCORS" and computer_pick == "PAPER":
            winner = "You"
        elif users_pick == "PAPER" and computer_pick == "ROCK":
            winner = "You"
        else:
            winner = "I"
        print("########## "+winner + " win")
        if not input("press any letter to continue, enter to quit playing"):
            break
        print("\n"*5)
    else:
        print("You picked nothing!")
        break

print("Lets play later, bye..")


    

