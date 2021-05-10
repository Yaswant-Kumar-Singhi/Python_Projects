# This is number guessing game
# Each player will get a limited number of chances to guess the game

'''IMPORTING LIBRARIES'''
import math 
import random

# TAKE LOWER RANGE
low = int(input("Enter Lower Range"))
# TAKE UPPER RANGE
upper = int(input("Enter Upper Range"))
# TOTAL NO OF CHANCES AS PER THE RANGE
t_chances = round(math.log(upper - low + 1, 2))
# GET A RANDOM NUMBER
x = random.randint(low,upper)

#COUNTER VARIABLE TO COUNT THE CHANCES
count = 0

#LOOP
while count < t_chances:
    count+=1
    y = int(input("Enter your guess"))

    if (x==y):
        print("Congrats you did in ",count," chances")
        break

    elif(y<x):
         print("Your guess is too small")
    
    elif(y>x):
         print("Your guess is too high")

if(count >= math.log(upper - low + 1,2)):
    print("You failed this time. Please come back again")


