# Function to find average marks

def find_average_marks(marks):
    sum_of_marks= sum(marks)
    total_subjects= len(marks)
    average_marks= sum_of_marks/ total_subjects
    return average_marks

# Calculate the grade and return

def compute_grade(average_marks):
    if average_marks >=80:
        grade=print("B")
    elif average_marks >=70:
        grade= print("C")
    elif average_marks >=60:
        grade= print("D")
    else:
        grade= print("F")
    return grade

marks= [55, 343, 3434, 34343]
average_marks= find_average_marks(marks)
print("Your average mark is", average_marks)


grade= compute_grade(average_marks)
print("Your grade is", grade)