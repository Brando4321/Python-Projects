numerator= 10
denominator= 0

try:
    numerator=int(input("Enter Numerator: "))
    denominator=int(input("Enter Denominator: "))
    
    result= numerator/denominator
    print(result)
    
    my_list= [1, 2, 3]
    i = int(input("Enter index; "))
    print(my_list[i])
except ZeroDivisionError:
    print("Try again :)")

except IndexError:
    print("can't be greater")    
print("Program ends")