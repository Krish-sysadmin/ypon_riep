import random, math

lower = int(input("Enter the guess range's lower value: "))
upper = int(input("Enter the guess range's upper value: "))

key = random.randint(lower, upper)
print("\nYou've only got", round(math.log(upper - lower + 1, 2)), " tries to guess the integer! gl! \n")

round = 0

while round < math.log(upper - lower + 1, 2):
    round += 1

    guess = int(input("Guess a number:- "))

    if key == guess:
        print("Congratulations you did it in ",
              round, " try")
        break
    elif key > guess:
        print("You guessed a number too tiny!")
    elif key < guess:
        print("You guessed higher :( ")

if round >= math.log(upper - lower + 1, 2):
    print("\nThe number was %d" % key)
    print("\tHope you enjoyed the game!")
