# ProgramTwoA.py
# Converts a Fahrenheit Temperature into its Celsius equivalent.
# By Christopher Wheeler
# September 14th,2025

#Display purpose of the program.
print("Lets convert Fahrenheit to celsius!")

#Prompt and receive input of the temperature in Fahenheit:
fahrenheit= float(input("\nWhat is your temperature in fahrenheit?: "))
#Calculate the Celsius equivalent:
celsius = (fahrenheit - 32) /1.8

#Display the Celsius equivalent
print(f"Your temperature in celsius is {celsius:.2f}°C")
