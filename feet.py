# Basic program that converts feet to meters
def main():
    user_feet=int(input("What's your height in feet? "))
    user_inches=int(input("What's your height in inches? "))
    result= convert_feet_to_meter(user_feet, user_inches)
    rounded_result= round(result,2)
    print(f"You are {rounded_result} meters tall!")


def convert_feet_to_meter(feet,inches):
    total_inches= feet* 12 + inches
    return total_inches *0.0254

main()