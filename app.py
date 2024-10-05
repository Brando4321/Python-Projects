
def main():
    user_inp= int(input("   Type in a number: "))
    result= fizz_buzz(user_inp)
    print(result)
    

def fizz_buzz(input):
    if input % 5==0 and input % 3==0:
        return f"FizzBuzz"
    if input % 3==0:
        return f"Fizz"
    if input %5==0:
        return f"Buzz"
    
    return input

main()
 