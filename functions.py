#functions

def say_greeting(name):
    print("Hello " + name)

#Class you want to display the grade of a given student.
#>=450 A, 400-450 : B, 350-400 C , any less than 350 D

students = ["John;300", "Ram;451", "QueenSara;250"]
days = ["Sunday", "Friday","Monday"]
def display_Deal_restaurant(day):
    # print(type(marks))
    match day:
        case "Sunday":
            price = 3.00
        case "Friday":
            price = 0.00
        case default:
            price = 2.00
    return str(price)

for day in days:
    print("Your deal on  " + day + " is " + display_Deal_restaurant(day))

def display_Grade(student):
    student_name = student.split(";")[0]
    marks = int(student.split(";")[1])
    #print(type(marks))
    if marks >= 450:
        grade = "A"
    elif marks <= 400:
        grade = "B"
    elif marks <= 350:
        grade = "C"
    else:
        grade = "D"
    print("Name: " + student_name + " Grade: " + grade)

for student in students:
    display_Grade(student)


