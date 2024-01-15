from random import randint

class Dice:
    @staticmethod
    def rolldice(count: int, num: int) -> int:
        rolled_dice = []
        for _ in range(count):
            rolled_dice.append(randint(1, num))
        return rolled_dice

print("\n--------------------------")
print("| DICE ROLLING SIMULATOR |")
print("--------------------------\n\n")

while True:
    print("Choose a dice to roll:\n")
    print("[ 1 ] - Roll a 4-sided single die")
    print("[ 2 ] - Roll two 4-sided dice (Double Dice)")
    print("[ 3 ] - Roll a 6-sided single die")
    print("[ 4 ] - Roll two 6-sided dice (Double Dice)")
    print("[ 5 ] - Roll a custom-sided die")
    print("[ 0 ] - Exit Simulator\n\n")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nRolling a 4-sided single die")
        print("Rolled result: ", Dice.rolldice(1, 4)[0], "\n")

    elif choice == 2:
        print("\nRolling two 4-sided dice (Double Dice)")
        print("Die 1: ", Dice.rolldice(1, 4)[0])
        print("Die 2: ", Dice.rolldice(1, 5)[0], "\n")

    elif choice == 3:
        print("\nRolling a 6-sided single die")
        print("Rolled result: ", Dice.rolldice(1, 6)[0], "\n")

    elif choice == 4:
        print("\nRolling two 6-sided dice (Double Dice)")
        print("Rolled results:")
        print("Die 1: ", Dice.rolldice(1, 6)[0])
        print("Die 2: ", Dice.rolldice(1, 6)[0], "\n")

    elif choice == 5:
        print("\nRolling a custom-sided die")

        sides = int(input("Enter the number of sides for the custom die: "))
        count = int(input("Enter the number of times to roll the die: "))
        
        print("\n")

        for index, i in enumerate(Dice.rolldice(count, sides), 1):
            print("Dice ", index, ": ", i)

        print("\n")

    elif choice == 0:
        print("\nExiting the Dice Rolling Simulator. Come back again!\n\n")
        break
    
    else:
        print("\nInvalid Input. Please check the option number and try again.\n\n")
