#The Walrus Operator in Python

#It allows you to assign a value to a variable within an expression.
#This can be used when you need to use a value multiple times in a loop, but don't
#to repeat the calculations

#Example of how we can use this operatot in a while loop

numbers = [1, 2, 4, 7, 8]

while (n := len(numbers)) > 0: #n is >0
    print(numbers.pop())
#Example 2
# without using walrus operator
# foods = list()
# while True:
#       food = input("What food do you like?:")
#       if food == "quit"
#           break

#using walrus operator
foods = list()
while (food := input("What food do you like?:")) !="quit":
    foods.append(food)
