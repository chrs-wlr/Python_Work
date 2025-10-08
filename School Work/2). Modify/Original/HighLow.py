# HighLow Application
# By: [replace with your name]
# [replace with current date]

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

else:
    print("You chose a different number from the computer!")
    print("The computer chose ", compNum)

