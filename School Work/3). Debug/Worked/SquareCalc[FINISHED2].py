# Module 02 Debug
# This program will prompt the user to enter the length of one side of a square.
# It should calculate and display both the area (side-squared) and perimeter (4xside).

# The program contains two errors.  Correct the errors so that the program runs as expected.
# Add comments to the lines modified to document and explain your changes.
# Upload the corrected version in Lamaku.
# Modified by:  Christopher Wheeler
# Date Modified:  09/14/25


print()
print("This program will calculate the area and perimeter of a square given the length of one side.\n\n")


sideLength = float(input("Enter the length of one side (in inches: "))#made it a float so that you are able to work with decimals

perimeter = 4 * sideLength
area = sideLength * sideLength #the l wasnt capital so i changed L switched area and perimeter


print("\nA square with a side length of", sideLength, "has an area of", area, "square inches and perimeter of", perimeter, "square inches.")
