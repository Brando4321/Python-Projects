name= input("Type your name: ")
print("Welcome", name, "to this adventure!")


answer= input("You are on a dirt road, it has come to an end and you can go left or right, where would you like to go ?  ").lower()

if answer== "left":
    answer= input("You come to a river, you can walk around it or swim across? Type walk to walk around or swim to swim accross: ")

    if answer== "walk":
        print("You walked for many miles, ran out of water and lost the game. ")
    elif answer =="swim":
        print("You swam across and were eaten by an alligator.")
    else:
        print("Not a valid option. You Lose!")
        quit()

elif answer== "right":
    answer= input("You come to a bridge, it looks wobbly,do you want to cross it? (cross/back)")

    if answer== "back":
        print("You go back and lose.")
    elif answer =="cross":
        answer= input("You crossed the bridge and meet a stranger. Do you talk to them (yes/no): ")

        if answer== "yes":
            print("You talked to the stranger and were given a bag of gold, YOU WIN!!!!!")
        elif answer== "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print("Not a valid option. You Lose!")  
    else:
        print("Not a valid option. You Lose!")
else:
    print("Not a valid option. You Lose!")

print("Thank you for trying", name)