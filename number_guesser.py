# Module random
import random

top_of_range= input("Type a number: ")

if top_of_range.isdigit():
    top_of_range= int(top_of_range)
    
    if top_of_range <= 0:
        print("Please insert a number greater than 0 next time: ")
        quit()
else:
    print("Please insert a number next time: ")
    quit()
     

random_number= random.randint(0, top_of_range)
guesses= 0

while True:
    guesses +=1
    User_guess= input("make a guess: ")
    # Verifiy if it is a number
    if User_guess.isdigit():
        User_guess= int(User_guess)
    
    else:
        print("Please insert a number next time: ")
        continue

    if User_guess== random_number:
        print("You got it right!")
        break
    
    elif: User_guess > random_number:
        print("you were above the number!")
    else:
        print("You were below the number!")
    
print("You got it in", guesses, "guesses")

