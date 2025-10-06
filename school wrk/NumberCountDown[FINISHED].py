# Number Count Down
# Modified By: Christopher Wheeler
# 9/29/2025

# Activity Modify: Module 04 Loops - Transform the following while loop
#    into an equivalent for loop producing the same output.

# Add comments to document and explain your changes.



count = int(input("Enter a number to start the count down: "))
#1.Added so that the count always makes it to the users input
count = count +1


#2.Made 0 my start value so the count starts at 0
for x in range (0,count):
        print (x)
print ("done?")




