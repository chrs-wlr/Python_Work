import random


userName = str(input("\nwhat is your name? ")).title()
#add a condition to the while while true doesnt have a condition its always true
#main outter loop
playAgain = "y" 
while playAgain == "y":
   comNum = random.randint(0,100)
   print(comNum)
   userNum = int(input(f"\nWhat number am i guessing between 1 and 100 {userName}?: "))

   
   while userNum > 100 or userNum < 0:
       print("\n\tCHOOSE A NUMBER BETWEEN 0 AND 100")
       userNum = int(input(f"What number am i guessing between 1 and 100 {userName}?: "))
        # this loop on the outside says while this isnt true repeat lines 16-31
        # inner loop 1       
   while userNum != comNum:
    

        #if checks for if the user guess right 
        if userNum == comNum:
            print(f"\ngood job i guessed {comNum} and u Picked {userNum}!")
        # checks for an incorrect guess
        else:
            print (f"\n\t  you guessed WRONG")
            print ("\n     Would you like to get a hint\n     or would you like to give up?")
            hint = str(input("\t   (continue? (y/n):"))
            if hint == "y":
                
                print ("ok lets continue!!!")
            
                if userNum > comNum:
                    print("your anser was too high")
                    userNum =int(input("What is your new number?: "))
                else:
                    print ("your number was too low: ")
                    userNum = int(input("what is your new number"))               
                    #allows for user to input again 
            userNum = int(input(f"\nWhat is your new number? {userName}?: "))
            #checks range
            while userNum > 100 or userNum < 0:
                 print("\n\tCHOOSE A NUMBER BETWEEN 0 AND 100")
               #userNum = int(input(f"What number am i guessing between 1 and 100 {userName}?: "))
            # allows for user to reinput a guess
   # playAgain = str(input("\n\t\tplay again? (y/n): "))

print (f"\n Have a good day and thanks for playing {userName}!")       