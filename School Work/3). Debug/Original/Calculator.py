# Calculator Application
# By: Christopher Wheeler
# 9/21/2025

# Activity Debug: Module 03 Conditionals - Find and correct two errors so the program will run as expected.
#      The program should accept two integers and prompt the user to select a menu option
#      and perform that computation.

# Add comments to document and explain your changes.




firstNum = int(input("Enter an integer: "))
secondNum = int(input("Enter another integer: "))

print()
print("What computation would you like to perform?")
print()
print(" 1. Add")
print(" 2. Subtract")
print(" 3. Multiply")
print(" 4. Divide")
print()

menuOption = int(input("Enter a number from the menu above: "))



if menuOption == 1:
    print("You selected addition. The sum is:  ", firstNum + secondNum) #changed "+" to ","

elif menuOption == 2:
    print("You selected subtraction. The difference is:  ", firstNum - secondNum)

elif menuOption == 3:
    print("You selected multiplication. The product is:  ", firstNum * secondNum)

elif menuOption == 4:
    print("You selected division. The quotient is:  ", firstNum / secondNum)

else:
    print("You have entered an invalid menu option!")
