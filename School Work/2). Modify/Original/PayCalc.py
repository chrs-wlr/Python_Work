# Module 02 Modify
# This program has the user enter two values representing the pay rate
# and number of hours worked for an hourly employee.  
# It then calculates and displays the gross pay (assuming no overtime or other pay)
# by multiplying the pay rate by the number of hours worked.

# Modify this program by improving the user interface so that it:
# 1. displays the program purpose/introduction,
# 2. displays an informative prompt for the user when entering both inputs and
# 3. displays a description of the output produced.

# Add comments to the lines modified to document your changes.
# Upload the corrected version in Lamaku.
# Modified by:  Christopher Wheeler
# Date Modified: 09/14/25


#Added a welcome message
print("Hello and welcome to PayCalc,\nLets find out your Grosspay!!!")

#added a promt to input hourly pay
payRate = float(input("\nPlease Input Your Hourly pay: "))

#added an input for hours worked
hours = float(input("Enter Your Hours Worked: "))

grossPay = payRate * hours

#added a ending message that displays grosspay
print(f"Your Grosspay is {grossPay}!!!")
