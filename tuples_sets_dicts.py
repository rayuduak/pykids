#TUPLES SETS DICTIONARY

#list
fruits = ['mango','berries',"mango"]
#tuple
tuple_fruits = ("apple","cherry","mango","apple")
print(tuple_fruits)
#cannot change
#tuple_fruits(1) = "blue berries"

# access data in tuple
print(tuple_fruits[0:2])

#how do we update a tuple
list_fruits = list(tuple_fruits)
list_fruits[1]="blue berry"
#print(list_fruits)
tuple_fruits = tuple(list_fruits)
#print(tuple_fruits)
for fruit in tuple_fruits:
    print(fruit)

tuple_fruits2 = ("grapes","pears")

tuple_fruits3 = tuple_fruits + tuple_fruits2
print(tuple_fruits3)

# please do exercise in tuples - https://www.w3schools.com/python/python_tuples_exercises.asp

#SETS  flower brace
fruits_set = {"mango","berry", "pears","mango"}
print(fruits_set)
fruits_set.add("banana")
print(fruits_set)
fruits_set.remove("mango")
print(fruits_set)
fruits_set.discard("strawberry")
print(fruits_set)

#please try union
fs2 = {"strawberry"}
fs3 = fs2.union(fruits_set)
print (fs3)


f1 = {"mango", "strawberry", "banana","orange"}
v1 = {"spinach", "potato","brocoli","mango"}

# how do we find kids who play both soccer and basketball
soccerteam ={"Sandy","Jacob","Bob","Sam"}
basketballteam = {"Sandy","Bob","Matt","santa"}
volleyballteam  = {"Sandy","Bob","santa","jonny"}

common_soccer_basketball = soccerteam.intersection(basketballteam)
common_volley_soccer_basket =common_soccer_basketball.intersection(volleyballteam)
print(common_volley_soccer_basket)

# please practice - https://www.w3schools.com/python/python_sets_methods.asp

# Dictionaries # flower brace, key and value
fruits_meaning = {
    "apple" : "apples are red green and yellow",
    "grapes": "they are sour and purple green"
}

cars_dictionary = {
    "brands" : "Honda",
     "model" : "odessy",
     "year"  : 2000
}
student_dictionary = {
    "id" : "121",
    "name" : "haris",
    "class": "5"
}

password_dict = {
    "www.amazon.com" : "rayudu|#$QASAD",
    "google" : "^W#WQ",
    "harrisroad" : "YYY@@@"
}

print(password_dict.get("amazon"))

