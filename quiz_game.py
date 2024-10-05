print("Welcome to my computer quiz!")

playing= input("Do you want to play my game? ")

if playing != "yes":
    quit()   
print("Okay! Let's play :) ")
score= 0
answer= input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct :)")
    score +=1

else:
    print("Incorrect!")
    
answer= input("What does RAM? ").lower()

if answer == "memory unit":
    print("Correct :)")
    score +=1

else:
    print("Incorrect!")

answer= input("What does graphics card? ").lower()

if answer == "graphical card":
    print("Correct :)")
    score +=1
else:
    print("Incorrect!")

answer= input("What does mean stand for ? ").lower()

if answer == "angry":
    print("Correct :)")
    score +=1

else:
    print("Incorrect!")
    
print("You got" +  str(score)  + "questions correct")
print("You got" +  str(score/4 *100)  + "%")
    