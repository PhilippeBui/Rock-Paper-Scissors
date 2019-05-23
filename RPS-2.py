#!/bin/python3
#simple rock/paper/scissors game

#import random function
from random import randint

#store player's input into var pchoice
player = input("r-rock, p-paper, s-scissors")

#store Computer's random integer between 1-3 into var cchoice
cchoice= randint(1,3)

#store computer's choice as string
if cchoice == 1:
  computer= 'r'
elif cchoice == 2:
  computer= 'p'
else:
  computer= 's'
  
#print player and computer's decisions
print("player:", player, " vs computer:", computer )
  
#compare each choice and print result of winner or tie
if player =='r' and computer == 1:
  print("tie")
  
elif player =="r" and computer == 2:
  print("computer wins")

elif player =="r" and computer == 3:
  print("player wins")
    
elif player =="p" and computer == 1:
  print("player wins")

elif player =="p" and computer == 2:
  print("tie")

elif player == "p" and computer == 3:
  print("computer wins")
  
elif player =="s" and computer == 1:
  print("computer wins")

elif player =="s" and computer == 2:
  print("player wins")

else:
  print("tie") 
