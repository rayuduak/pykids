#lists and tuples

#list can be modified
fruit = "apple"
fruits = ["mango", "strawberry", "banana","orange"]
vegs =   ["spinach", "potato","brocoli","mango"]

print(fruits)
print(fruits[1])
fruits[1]="cherry"
fruits.insert(1,"orange")
fruits.remove("banana")
fruits.extend(vegs)
print(fruits)
#insert, extend
#when you are playing game , Player1=rayudu
players =["harsith", "manideep","ishan"]

print(players.index("ishan"))
#players.remove("Harsith")
players.insert(0,"pranay")
print(players)
#players.pop()
#players.clear()

#Question: Print the players with order mean number  in the begining
# 1. pranay 2.Hars...
# iterate loop
score = 9
for player in players:
    print(str(players.index(player)+1) + " : " + player + "[" + str(score) + "]")

#Homework: Question - what are the common items in the fruits and vegs array/list
for f in fruits:
    for v in vegs:
        if str(f) == str(v):
            print(f)


# homework - try to use how to sort the list, how to reversort, copy one list to othrs, find all other methods

# https://www.w3schools.com/python/python_lists.asp
