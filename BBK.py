from tkinter import *
import random


lst=['rock','paper','scissor']
res=random.choice(lst)

def new_game():
    a=input("Enter paper, rock or scissor : ")
    if res==a:
        print("Oppnent: "+res)
        print("Draw")
    else:
        if res=="paper" and a=="rock":
            print("Oppnent: "+res)
            print("Lose")
        elif res=="scissor" and a=="rock":
            print("Oppnent: "+res)
            print("Win")
        elif  res=="scissor" and a=="paper":
            print("Oppnent: "+res)
            print("Lose")
        elif res=="rock" and a=="paper":
            print("Oppnent: "+res)
            print("Win")
        elif res=="paper"and a=="scissor":
            print("Oppnent: "+res)
            print("Win")
        elif res=="rock"and a=="scissor":
            print("Oppnent: "+res)
            print("Lose")

def play_again():
    response=input("Do you want to try again ? Pls enter Yes or No :")
    response=response.lower()
    if response=="yes":
        return True
    if response=="no":
        return False

new_game()

while(play_again()):
    new_game()

print("Good Bye!")