import random 
answer = str(input("TEST YOUR FATE....(y/n)")).lower()

if answer == "n":
    print("Thats too bad...")
else:
    #generate a random number to represent the coin
    coinFlip = random.randint(1,2)
    #state conditions
    if coinFlip == 1:
        coinFlip = "HEADS"
    else:
        coinFlip = "TAILS"
    #print to close the loop i think?
    print (f"{coinFlip} is your FATE")

#redefine choice outside the loop 
choice = str(input("continue?(y/n) ")).lower()    

#define y conditions in while
while choice == ("y"):
    coinFlip = random.randint(1,2)

    if coinFlip == 1:
         coinFlip = "HEADS"
    else:
         coinFlip = "TAILS"

#keep stuff like this outside the else block
    print (f"{coinFlip} is your FATE")
    choice = str(input("continue?(y/n) ")).lower()
         
print ("ENJOY YOUR FATE!!!!!")

    

