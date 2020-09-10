#Import functions

import random

while True:
    user = input("Please select \n Rock, \n Paper, \n Scissors \n Input: ")
    cpuser = random.choice(['Rock', 'Paper', 'Scissors'])

    #conditioning using IF statements
    if user == cpuser:
        print("Tie")
    elif user == "Rock":
        if cpuser == "Paper":
            print("Computer wins!", cpuser, "beats" , user)
        else:
            print("Player wins", user, "beats", cpuser)
    elif user == "Paper":
        if cpuser == "Scissors":
            print("Computer wins!", cpuser, "beats", user)
        else:
            print( "Player wins", user , "beats", cpuser)
    elif user == "Scissors":
        if cpuser == "Rock":
            print("Computer wins!", cpuser, "beats", user)
        else:
            print("Player wins", user, "beats", cpuser)
    else:
        print("Error, please check spelling")

#Just for fun!!

