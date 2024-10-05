import random

rand_num= random.randint(1,5)
def main():
    num_1= int(input("Insert a number: "))
    num_2= int(input("Insert another number: "))
    result= calc_multiply(num_1, num_2)
    print(f"Your result is {result}!")

    option= input("You will now play a guessing game type (P) to play or type (Q) to to quit: ").capitalize()
    num_guess1= calc_guess(option)
    print(num_guess1)

def calc_multiply(n1, n2):
    return n1 * n2


def calc_guess(option):
    if option == "Q":
        quit("Ok thanks for playing")
    else:
        while True:
            try:
                user_guess= int(input("Type in your guess number from (1-5): "))
                if user_guess== rand_num:
                    print("Good job you guessed the number :)")

                    break
                else:
                    print("Sorry you have not guessed the number try again :(")
            except ValueError:
                print("Please type in an integer not a word :)")

main()