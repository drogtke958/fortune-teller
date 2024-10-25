# Keily Drogt
# Oct 24, 2024
# Fortune Teller

import random
import sys
import time

fortunes = ["You are a winner!", "A secret admirer will soon send you a sign of affection!", "The one you love is much closer than you think!", "Good things will happen to you by the end of the day today!", "Fame and fortune will be yours if you take the time to learn Python!", "I'm just a computer program, and have no magical powers!"]
magic_colors = ["Blue", "Red", "Green", "Yellow"]

user_name = input("Enter your name: ")

print(f"Welcome to my Python Fortune Teller program, {user_name}!\n")

question = input(f"do you want me to tell you your fortune? {user_name}?\n").lower()
time.sleep(2)

if question in ["y", "yes"]:
    time.sleep(1)
    color = input("Okay! In order to get your fortune, please input a magic color(Blue, Red, Green, Yellow): \n").lower()
    
    time.sleep(1)
    print("Getting your fortune...\n")
    time.sleep(2)
    print(f"Here is your fortune, {user_name.title()}: \n")
    time.sleep(1)

    if color in magic_colors: 
        index = random.randint(0, len(fortunes) -1)
        print(fortunes[index])
    else:
        print("Choose a magic color of either 'Blue', 'Red', 'Green', or 'Yellow'\n")
        time.sleep(1)
        print("Once you have entered a magic color, I will reveal your fortune!\n")
else:
    print(f"Thank you for playing my fortune teller game, {user_name}!\n")
    print("Goodbye!\n")
    sys.edit
