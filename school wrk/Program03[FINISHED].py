# Program 03
# This program allows the user to play Jan-Ken-Po against the computer.
# By: Christopher Wheeler
# Date 9/21/2025

import random

print("Let's play Jan-Ken-Po!\n")
userChoice = str(input("Make your choice (R for rock/P for paper/S for scissors): ")).upper()
compChoice = random.randint(1,3)


#Display "The computer chose xxxx" where xxxx is rock when compChoice is 1,
#xxxx is paper when compChoice is 2, and xxxx is scissors when compChoice is 3.


#Converting comp number ot words
if compChoice == 1:
    compChoice = ("ROCK")
elif compChoice == 2:
    compChoice = ("PAPER")
else:
    compChoice = ("SCISSORS")

#converting user choice to text
if userChoice == "R":                     
    userChoice = ("ROCK")
elif userChoice == "P":
    userChoice = ("PAPER")
else:
    userChoice = ("SCISSORS")
    







#added user friendly "you picked {userChoice}" outcome option
if compChoice == userChoice:
    print (f"I picked {compChoice} you picked {userChoice} its a DRAW")
elif (userChoice == "ROCK" and compChoice == "SCISSORS") or (userChoice == "PAPER" and compChoice == "ROCK") or (userChoice == "SCISSORS" and compChoice == "PAPER"):
    print(f"I picked {compChoice} you picked {userChoice} you WIN perfect")
elif (userChoice == "PAPER" and compChoice =="SCISSORS") or (userChoice == "SCISSORS" and compChoice == "ROCK") or (userChoice == "ROCK" and compChoice == "PAPER"):
    print(f"I picked {compChoice} you picked {userChoice} you LOSE")
else:
    print("Input one of the options plz")
    
    





#If the user chose R for rock, display the user's result.

