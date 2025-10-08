# Miles to Kilometers Conversion
# This program converts a distance in miles
# to its equivalent distance in kilomters.
# By: Michael Bauer
# August 20, 2020

KM_PER_MILE= 1.609

print("This program converts a distance in miles to its")
print("equivalent distance in kilometers.")

print()
print()
miles = float(input("Enter miles:"))

km = miles * KM_PER_MILE


print("\n\nThe distance in kilometers", km)
