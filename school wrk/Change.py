# Change Program
# By: ICS 110P Class
# August 29, 2018

QUARTER = 25
DIME = 10
NICKEL = 5
change = float(input("Enter the amount of change: "))
quarters = change // QUARTER
change = change % QUARTER
dimes = change // DIME
change = change % DIME
nickels = change // NICKEL
pennies = change % NICKEL


print("Please give the customer " , quarters, " quarters, " , dimes, " dimes, " ,
      nickels, " nickels, and ", pennies, " pennies.")
