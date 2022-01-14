import random

let_me_guess = input("Try to guess what number would be randomly generated, the range is 1 and 4: ")
key = random.randrange(1, 4)

#check if guess is within randrange (still needs adjustments)
def ram_range():
    try:
        int(1) <= int(let_me_guess) <= int(4)
        check_guess()
    except:
        quit()

ram_range()

#out result of user guess
def check_guess():
    if  int(let_me_guess) == int(key):
        print("True")
    else:
        print("False")
        print("The random number generated was", key)

check_guess()
