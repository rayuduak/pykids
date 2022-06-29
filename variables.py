# variables
"""
In python a variable is created when a value is assigned to it.
example:  
"""
x = 2
print(x)

"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
 """
 
#  Correct examples: fruit, count_of_fruits, firstName, last_Name, Name2, _vegetables_
#  Incorrect examples:   2lastname, first-last, middle name

#Multiple assignments at one shot
a, b, c = 10, 20, 30

#global variables: declAre varible outside a def and use them inside and able to change the same variable inside def
#example1:

print("\nexample1: ")
compliment = "You are amazing"
def greeting():
    print(compliment)
greeting()


#example2:
print("\nexample2")
compliment = "You are amazing"
def greeting():
    compliment= "You are superkid"
    print(compliment)

greeting()
print(compliment)
