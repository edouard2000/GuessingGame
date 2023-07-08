#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

attempts = 0
your_guess = 0

def levelChoice():
    global attempts
    level = input("Choose between 'Hard' or 'Easy': ").lower()
    if level == "hard":
        attempts = 5
    else:
        attempts = 10
        
def GuessesComparison():
    global attempts, your_guess
    number_list = list(range(1, 101))
    guess = random.choice(number_list)
    your_guess = int(input("Type Your Guess: "))
    
    if guess == your_guess:
        print(f"{your_guess} is the right one")
        attempts -= 1
        attempts = 0  # End the game when the guess is correct
    elif guess > your_guess:
        print(f"{your_guess} is too low")
        attempts -= 1
    elif guess < your_guess:
        print(f"{your_guess} is too high")
        attempts -= 1
    else:
        print(f"{your_guess} is out of scope")
        attempts -= 1
        
def start():
    print("Welcome to GuessingNumber")
    print("You can guess between 1 and 100")
    input("Type any key to proceed: ")
    levelChoice()

start()
while attempts != 0:
    GuessesComparison()
    print(f"Attempts remaining: {attempts}")

choice = input("Do you want to start? 'Yes' or 'No': ").lower()

if choice == "yes":
    start()
    while attempts != 0:
        GuessesComparison()
        print(f"Attempts remaining: {attempts}")
else:
    print("See you soon")


# In[ ]:




