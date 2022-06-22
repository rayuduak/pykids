#strings
"""
Ex:
1.
Harsit grade6 nice A,Bushra grade5 good A+,Ishan grade6 Awesome B
Print name , grade and comment all in eachline
Harsit grade6 nice A
Bushra grade5 good A+
Ishan grade6 Awesome B

2. Mandeep Mutyala Chicago
I want all lastnames capital letter/uppercase and which city 

3. United States of America , Dominican Republic
I want the first letter of each word. USA and DR

"""

name = "United States of America"
#a string is array of characters
#  [U][n][i][t][e][d] 0.1....
print("Original:" + name)
print("Ishan" + " Grade6")
print(name[0] + name[7] + name[17])
print(name[0:6])
#slice
print(name[:6])
print(name[7:])

#slice backwards
print(name[-5:-2])
# Case manipulation , upper or lower

print("Lower: " + name.lower())
print("Upper: " + name.upper())
sampletext =" Hello this is python kids class     "
print(sampletext)
print(sampletext.strip() )
print(sampletext.replace("s", "S"))


line = "Bushra grade5 good A+,Ishan grade6 Awesome B,Harsit grade6 nice A"
print(line)
splittedline = line.split(",")
print(splittedline)
print(splittedline[0])
print(splittedline[1])
print(splittedline[2])

#format

firstname = "Alex"
lastname = "Jayakumar"
city = "Concord"

studentDetails = "The student firstname is {1}  lastname is {0} and he is from the city {2}"
print(studentDetails)
print( '\'' + studentDetails.format(lastname,firstname,city))
print(len(line))
print(line.index("A+"))

newstring = input("enter something")
if newstring.isalpha() :
    print("you entered alphabets")
else:
    print("you entered numeric")

"""
https://www.w3schools.com/python/python_strings_methods.asp
https://www.w3schools.com/python/python_strings_exercises.asp
"""
