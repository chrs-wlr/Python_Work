# Program 03
# This program allows the user to play Jan-Ken-Po against the computer.
# By: Christopher Wheeler
# Date 9/26/2025

import random

print("Let's play Jan-Ken-Po!\n")

#1.placing "while True" over the whole code makes the whole code a loop rather than makng each section a loop doing it that way was too complicated
#  i used "while true" instead of "while" because its my understanding that i can set my own escape by adding break rather than making the escape a conditional
#  i am not to sure as to why u would use while true instead of while for every condition however this wouldnt work without the while true i dont completly understand and am still a bit confused

while True:
#2.Ask for User Input and Check for validation
   userChoice = str(input("\nMake your choice (R for rock/P for paper/S for scissors): ")).upper()
#3.extended a few of my user choices
   #If the user chose R for rock, display the user's result.

   while userChoice not in ("R","P","S","ROCK","PAPER","SCISSORS"):
       print("\n\t\tnope try again")
       userChoice = str(input("\nMake your choice (R for rock/P for paper/S for scissors): ")).upper()


   compChoice = random.randint(1,3)


#Display "The computer chose xxxx" where xxxx is rock when compChoice is 1,
#xxxx is paper when compChoice is 2, and xxxx is scissors when compChoice is 3.


#4.Converting comp number ot words
   if compChoice == 1:
       compChoice = ("ROCK")
   elif compChoice == 2:
    compChoice = ("PAPER")
   else:
       compChoice = ("SCISSORS")

#5.converting user choice to text
   if userChoice == "R" or userChoice == "ROCK":                     
       userChoice = "ROCK"
   elif userChoice == "P" or userChoice == "PAPER":
       userChoice = "PAPER"
   else:
       userChoice = ("SCISSORS")
    


   if compChoice == userChoice:
#6.added user friendly "you picked {userChoice}" outcome option
       print (f"\n I picked {compChoice} you picked {userChoice} its a DRAW")
   elif (userChoice == "ROCK" and compChoice == "SCISSORS") or (userChoice == "PAPER" and compChoice == "ROCK") or (userChoice == "SCISSORS" and compChoice == "PAPER"):
        print(f"\nI picked {compChoice} you picked {userChoice} you WIN perfect")
   elif (userChoice == "PAPER" and compChoice =="SCISSORS") or (userChoice == "SCISSORS" and compChoice == "ROCK") or (userChoice == "ROCK" and compChoice == "PAPER"):
          print(f"\nI picked {compChoice} you picked {userChoice} you LOSE")
   else:
       print("error")


   answer = str(input("\n\tplay again? (y/n): ")).lower()
   if answer == "n":
        print("\n Thanks for playing Rock Paper Scissors!!!!")
#7.added break command to stop the program from repeating itself 
        break






































#ASCII adds a little fun!
print("                                ")
print("                                ")
print("                                ")
print("    ▄██████████████████████▄    ") 
print("    █                      █    ")
print("    █ ▄██████████████████▄ █    ")
print("    █ █                  █ █    ")
print("    █ █                  █ █    ")
print("    █ █  █            █  █ █    ")
print("    █ █     ▄▄▄▄▄▄▄▄     █ █    ") 
print("    █ █     ▀▄    ▄▀     █ █    ")
print("    █ █       ▀▀▀▀       █ █    ")
print("    █ █                  █ █    ")   
print(" █▌ █ ▀██████████████████▀ █ ▐█ ")
print(" █  █                      █  █ ")
print(" █  █ ████████████  ██     █  █ ")
print(" █  █                      █  █ ")
print(" █  █               ▄      █  █ ")
print(" ▀█▄█    ▐█▌    ▄███▄ ██   █▄█▀ ")
print("   ▀█  █████               █▀   ")
print("    █   ▐█▌          ██▄   █    ") 
print("    █              ▐████▌  █    ")
print("    █ ▄▄▄ ▄▄▄       ▀██▀   █    ")
print("    █                      █    ")
print("    ▀██████████████████████▀    ")
print("        ██            ██        ")
print("        ██            ██        ")
print("        ██            ██        ")
print("        ██            ██        ")
print("       ▐██            ██▌       ")
