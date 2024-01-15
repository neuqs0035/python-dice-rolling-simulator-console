from random import randint

class Dice:
 
    def rolldice(count : int,num: int) -> int:

        rolled_dice = []

        for i in range(count):
            rolled_dice.append(randint(1,num))


        return rolled_dice


print("\n--------------------------")
print("| DICE ROLLING SIMULATOR |")
print("--------------------------\n\n")


while True:

    print("[ 1 ] - Roll 4 Sided Single Dice")
    print("[ 2 ] - Roll 4 Sided Double Dice")
    print("[ 3 ] - Roll 6 Sided Single Dice")
    print("[ 4 ] - Roll 6 Sided Double Dice")
    print("[ 5 ] - Roll Custom Dice")
    print("[ 0 ] - Exit Simulator\n\n")

    choice = int(input("_ : "))

    if choice == 1:

        print("\n\n4 Sided Single Dice\n\n")

    elif choice == 2:

        print("\n\n4 Sided Double Dice\n\n")

    elif choice == 3:

        print("\n\n6 Sided Single Dice\n\n")

    elif choice == 4:

        print("\n\n6 Sided Double Dice\n\n")

    elif choice == 5:
        print("\n\nCustom Sided Dice\n\n")

    elif choice == 0:

        print("\n\nProgram Exited , Come Back Again\n\n")
        break
    
    else :

        print("\n\nInvalid Input , Please Check Option Number And ReEnter\n\n")