#======================================================
# Name: Hangman.py
# Description: This program runs a hangman game
# Creation Date: 2023-09-21
# Created By: tristan sotello
#pizza time 
# Change Log
# Date Changed       Changed By      What changed
#======================================================

import random
import os
import time
import signal

def user_lower_case():
    user_input = input('Guess a character: ')
    return user_input.lower()


#wordlist for program to chose from
wordlist = ['hallmark', 'eagles', 'networking', 'hardware', 'technology', 'cloud', 'zebra']

#program selecting random word 
word = random.choice(wordlist) 

word_size = len(word)
#welcoming user 
name = input('whats your name: ')

print ('hello', name,'time to play hangman!')

time.sleep(3)
print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("...")
time.sleep(1)
print("....")
time.sleep(1)
print(".....")
time.sleep(1)
print("......")
os.system('cls' if os.name =='nt' else 'clear')

#setting var for user to guess word
user_guess = ''

endgame = 1

turns = 5

fail = 0

#loop for game to find ____ for word
array = []
correct_characters = list(word)
for i in word:
    array.append('_')

print (*(array))

#loop for game 
while True:
    if array == correct_characters:
        endgame = 0
        break
    index = 0
    guess = user_lower_case()

    guess += user_guess
    if not guess.isalpha():
        print ('you didnt input a correct character')
        fail += 1
    elif guess in array:
        print ('you already guessed this!')
        print ('you have', turns - fail, 'guesses left')
        fail +=1

    #if already guessed
    #lettter exist
    #pop insert on space occored
    for letter in correct_characters: 
        if guess in letter:
            array.pop(index)
            array.insert(index, guess)
            index += 1
        else:
            index += 1

    print (*(array))
    #if guess is not found in random word
    if guess not in word:
        fail += 1
        print ('wrong')
        print ('you have', turns - fail, 'guesses left')
        if turns == fail:
            print ("you lose word was", word)
            endgame = 2
#game ending 
if endgame == 0:
    print ('congrats you won')
    user_response = input('what do you wanna say to the folks back home')
    print ('audince laughs at incredibly uniqe response')
if endgame == 2:
    print ('audince laughs at users inabllity to preform')
