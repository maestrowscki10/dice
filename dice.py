import random
roll_dice = input("do you want to roll dice ?y/N: ")

if roll_dice == "Y" or roll_dice =="y":

    posiblle_results = [1, 2, 3, 4, 5, 6]
    result = random.choice(posiblle_results)
    print("Result of dice rolling is : " + str(result))