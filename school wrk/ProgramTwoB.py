# ProgramTwoB.py
# Converts a volume in gallons into its liters equivalent.
# By Christopher Wheelr
# September 14th, 2025

#Display purpose of the program.
print("Lets Convert Gallons to Liters!")

#Prompt and receive input of the volume in gallons:
gallons = float(input("\nPlease enter the number of gallons.: "))

#Calculate the liters equivalent:
liters = 3.78541 * gallons

#Display the liters equivalent
print(f"You will have {liters:.2f} liters")
