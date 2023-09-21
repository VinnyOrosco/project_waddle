#======================================================
# Name: Geuss the number.py
# Description: This program runs a simple guess the number game 
# Creation Date: 2023-09-08
# Created By: tristan sotello
#
# Change Log
# Date Changed       Changed By      What changed
#  2023,09,08         tristan s.     changed variables 
# ^^^^^^PUT WHAT YOU CHANGED AND WHY^^^^^^^^^
#======================================================

import random

#this lines is added just for fun so the participants feel more engaged
player_name = input('Identify your self! ')

#this line gives you the 'random' input number from 1-50
n = random.randint (1,50)

#again this is just for some more fun
print('Very well, '+ player_name + 
      '. If you succesfully guess my number between 1 and 50. ' +
      'You win bragging rights!')

#this is the starting range showing that you start at the beginning not try number 3 or so
guess_chances = 1
while guess_chances <= 5:
    print('Enter an integer of your liking:')

    num = input()

    if num[0] == '-': #check for '-' in case -1
        print('Do you understand the assignment! Try again, FOOL!')
    else:
        if str.isdigit(num):
            num = int(num) #convert it to an integer
            #these next commands will differentiate between where you are too low or too high of a guess and the else break will go to if guess == number
            if num < n:
                print('Too Low! Try again you heathen.')
            elif num > n:
                print('Too HIGH! Try again you heathen.')
            else:
                break
        else:
            print('Art thou educated? That is not a number! Guess again!')
        
    guess_chances += 1
#End of While Loop

#when the answer is correct then the participate will recieve the following
if num == n:
    print('You have answered honorably, ' + 
          player_name +'! it took you ' +  
          str(guess_chances) + ' tries!')
else:
    print('You have dishonored the king! To the dungeon with you!')

print('The number was:', n)
print('GAME OVER MAN! GAME OVER!')
