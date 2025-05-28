# Exercise 91: Problem Solving : Snake, Water, Gun Game

# Snake, Water or Gun
#   0     1        2

# 00 draw, 01 0>, 02 <2, 12 1>

import random
my_score = 0
comp_score = 0
rounds = 3

for i in range(1, rounds+1):
    print(f"Round {i}" )
    user = input("Enter choice : Snake, Water or Gun:  ").capitalize()
    list = ["Snake","Water", "Gun"]
    comp = random.choice(list)
    print("You entered: ",user)
    print("Computer entered: ",comp)
    if user not in list:
        print("Invalid input. Please enter Snake, Water, or Gun.")
        continue
    if(user==comp):
        print(f"Round {i} Draw")
    elif(user=="Snake" and comp=="Water") or (user=="Water" and comp=="Gun") or (comp=="Snake" and user=="Gun"):
         print("You won this Round")
         my_score+=1
    elif(comp=="Snake" and user=="Water") or (comp=="Water" and user=="Gun") or (user=="Snake" and comp=="Gun"):
         print("Computer won this round")
         comp_score+=1   
print("your score is:",my_score)
print("computers score is:",comp_score)
if(my_score > comp_score):
    print("You are the final winner")
elif(my_score < comp_score):
    print("You Lost")
else:
    print("It's a tie")





