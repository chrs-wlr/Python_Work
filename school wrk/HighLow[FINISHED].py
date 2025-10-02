# HighLow Application
# By: Christopher Wheeler
# 9/21/2025

# Activity Modify: Module 03 Conditionals - Modify the conditional statement so it will compare and inform the user
#       if their number is higher or lower than the computer's number.

# Add comments to document and explain your changes.


import random

print("\n")
userNum = int(input("Enter a number between 1-50: "))
compNum = random.randint(1,50)

print()

if userNum == compNum:
    print("You chose the same number as the computer!")
    print("the computer also chose",userNum )
elif userNum > compNum:
    print("your number was HIGHER than the computers!")#added an option for the computer to respond to a higher number should the user choose a higher int
    print("the computer chose", compNum)
elif userNum < compNum:
    print("Your number was LOWER than the computer!")#added an option for the computer to respond should the user pick a lower number
    print("the computer chose", compNum)
else:
    print("You chose a different number from the computer!")
    print("The computer chose ", compNum)

