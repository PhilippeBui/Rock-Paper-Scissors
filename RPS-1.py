#!/bin/python3
#simple rock/paper/scissors game

#import random function
from random import randint

#store player's input into var pchoice
pchoice = input("r-rock, p-paper, s-scissors")

#store Computer's random integer between 1-3 into var cchoice
cchoice= randint(1,3)
 
#display user and computer choices - computer choice will be int
print("player: ", pchoice, " vs computer: ", cchoice )

# Method 1- display computer choice as string
if cchoice == 1:
  print("computer chose rock")
elif cchoice == 2:
  print("computer chose paper")
else:
  print("computer chose scissors")
  
# Compare each choice and print result of winner or tie
if pchoice =='r' and cchoice == 1:
  print("tie")
  
elif pchoice =="r" and cchoice == 2:
  print("computer wins")

elif pchoice =="r" and cchoice == 3:
  print("player wins")
    
elif pchoice =="p" and cchoice == 1:
  print("player wins")

elif pchoice =="p" and cchoice == 2:
  print("tie")

elif pchoice == "p" and cchoice == 3:
  print("computer wins")
  
elif pchoice =="s" and cchoice == 1:
  print("computer wins")

elif pchoice =="s" and cchoice == 2:
  print("player wins")

else:
  print("tie") 
