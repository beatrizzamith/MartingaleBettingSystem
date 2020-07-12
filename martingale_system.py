import random


def roll_dice():
    """Returns true if the dice is red or false if it's black."""
    roll = random.randint(1, 100)
    if roll % 2 == 0:
        return True
    else:
        return False


def place_bet():
    """Places the user's bet and returns true if it bet red or false if it bet black"""
    print("Insert the letter correspondent to the colour you wish to bet on.")
    bet = input("R - Red\nB - Black")
    if bet == "R":
        return True
    elif bet == "B":
        return False
    else:
        print("That isn't an option.")
        return place_bet()


funds = int(input("Input funds:"))
initial_bet = int(input("Input initial bet:"))
while initial_bet > funds:
    print("It's not possible to bet more than you possess.")
    initial_bet = int(input("Input a lower betting value:"))

amount = initial_bet
status = True
value = True

# while funds > 0: # Stops if the user goes broke.
for x in range(100):  # Stops after running the code 100 times.
    #  value = place_bet()  #  Asks the user which colour to bet on.
    print("You're betting " + str(amount) + "€.")
    if roll_dice() != value:
        print("You've lost the round.")
        funds -= amount
        if funds < 0:
            break
        print("You currently have " + str(funds) + "€.")
        amount *= 2
        if amount > funds:
            print("You can't bet more than you have.")
            break
        funds -= amount
        if funds < 0:
            break
    else:
        print("You've won the round.")
        funds += amount
        print("You currently have " + str(funds) + "€.")
        amount = initial_bet

print("\nYou finished the game with " + str(funds) + "€.")
if funds <= 0:
    print("You're broke bitch.")
