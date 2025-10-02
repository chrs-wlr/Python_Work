# Print Odd Numbers
# TASK: Find and correct three errors so the program will run as expected.
# The program should print all odd numbers including the values in numOne and maxLimit if odd.
# Modified By: Chirstopher Wheeler
# 9/29/25
            



numOne = 1       #print should include this value if odd
maxLimit = 51    #print should include this value if odd

#Checks if numOne is less than max rather than greater
while(numOne < maxLimit):
    #== is for even != is for odd    
        if numOne%2 != 0:
                print(numOne)
      # The - was causing the program to cound down into the negatives
        numOne = numOne + 1
print (numOne)