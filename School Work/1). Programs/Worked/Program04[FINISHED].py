import random


userName = str(input("\nwhat is your name? ")).title()
#add a condition to the while while true doesnt have a condition its always true
#main outter loop
playAgain = "y" 
while playAgain == "y":
   comNum = random.randint(0,100)
   userNum = int(input(f"\nWhat number am i guessing between 1 and 100 {userName}?: "))

   
   while userNum > 100 or userNum < 0:
       print("\n\tCHOOSE A NUMBER BETWEEN 0 AND 100")
       userNum = int(input(f"What number am i guessing between 1 and 100 {userName}?: "))
        # this loop on the outside says while this isnt true repeat lines 16-31
        # inner loop 1       
   while userNum != comNum:
    

        #if checks for if the user guess right 

        # checks for an incorrect guess

        print (f"\n\t  you guessed WRONG")
        print ("\n     Would you like to get a hint\n     or would you like to give up?")
        hint = str(input("\t   (continue? (y/n):"))
        if hint == "y":
            
            print ("\n\t   ok lets continue!!!")
        
            if userNum > comNum:
                print("\t your answer was too HIGH")
                
            else:
                print ("\t your answer was too LOW: ")
                               
                #allows for user to input again 
        userNum =int(input("\n\tWhat is your new number?: ")) #places it w the if so that ????        
        #checks range
        while userNum > 100 or userNum < 0:
                print("\n\tCHOOSE A NUMBER BETWEEN 0 AND 100")
            #userNum = int(input(f"What number am i guessing between 1 and 100 {userName}?: "))
        # allows for user to reinput a guess
# playAgain = str(input("\n\t\tplay again? (y/n): "))
   print(f"\nGOOD JOB i guessed {comNum} and u Picked {userNum}!")
   playAgain = str(input("play again? (y/n)"))
   #lets user exit the loop
   #lines up with the while userNum != comNum:

print (f"\n Have a good day and thanks for playing {userName}!")       

        #if userNum == comNum: # for it to be true it has to be outside the while loop will never reach while inside loop conditition
            #print(f"\ngood job i guessed {comNum} and u Picked {userNum}!")
