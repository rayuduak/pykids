#what is a class, object
#how to use those classes , between two classes
# init function and why and how to use it
#school Project
# students, teachers, classrooms, schedule, staff

#CAR project
#accelration, brakes, start, stop, move, opendoors, gears, reverse
import sys


class Student:
    def __init__(self,name):
        self.name = name
    def studentdetails(self, sid, age):
        self.sid = sid
        self.age = age

class Teacher:
    def __init__(self, name, cls):
        self.name = name
        self.cls = cls
    def teacherid(self,tid):
        self.tid = tid

teacher1 = Teacher("John","Math")
teacher1.teacherid(100)
teacher2 = Teacher("Sam","English")
teacher2.teacherid(102)


class School:
    def __init__(self):
        selection = input("Select what you like to do? 1:student, 2:teacher, 3:schedule, 4:quit ")

        if selection=="1":
            name= input("Enter student name: ")
            sid = input("Enter id: ")
            age = input("Enter age: ")
            st1 = Student(name)
            st1.studentdetails(sid, age)
            print(st1.name + "-" + st1.sid + "=" +  st1.age)
        elif selection=="2":
            name = input("Enter teacher name: ")
            cls = input("Enter age: ")
            t1 = Teacher(name, cls)
            print(t1.name + "-" + t1.cls)
        elif selection == "3":
            arr_teachers = [teacher1, teacher2]
            for a in arr_teachers:
                print(a.name)
            first_period_teacher = input("which teacher do you want to schedule")
            selected_teacher = False
            for a in arr_teachers:
                if first_period_teacher==a.name:
                    selected_teacher = True
            if selected_teacher==False:
                    print("You did not select the right teacher")
            else:
                    print("Teacher " + first_period_teacher + " is scheduled" )
        else:
            sys.exit()

## Select what you want to do?

schoo1 = School()

"""
student1 = Student("ray", 1, 12)
teacher1 = Teacher("John","Math")
teacher2 = Teacher("Sam","English")

arr_teachers = [teacher1,teacher2]
for a in arr_teachers:
    print(a.name)
"""

