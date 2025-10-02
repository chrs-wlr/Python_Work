#3-4. guest list
#Make a list that includes atleast three people toud like to invite to dinner
# then use your list to print a message to each person inviting them to dinner 

crew = ['driss','ion','rory','kc']

print (f"{crew} you are now invited to the greatest pirate crew of all time The Dread Pirates!!!") 

#3-5. changing guest list
# you just heard that one of your guests cant make it 
#add a print call

missing = crew.pop(0)

print(f"\nhowever {missing.title()} cannot make it...")

#the "sort()" method changes the order of the list permanently

crew.sort()
print(crew)

#you can put it in reverse with the "reverse=True" method
crew.sort(reverse=True)
print(crew)