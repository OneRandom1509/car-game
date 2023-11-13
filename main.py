from time import sleep
import random
from random import randrange

def player1():
    s1 = 0
    timePassed1 = 0

    while (s1 < distance):
        s1 += random.randrange(0,3)
        print('Player 1: ' + ' ' * s1 + '>' + ' ' * (distance - s1) + '|', end = '\r')
        timePassed1 += 1
        sleep(1)
    print('\n')
    return(timePassed1, s1)

def player2():
    s2 = 0
    timePassed2 = 0

    while (s2 < distance):
        s2 += random.randrange(0,3)
        print('Player 2: ' + ' ' * s2 + '>' + ' ' * (distance - s2) + '|', end = '\r')
        timePassed2 += 1
        sleep(1)           
    print('\n')  
    return(timePassed2, s2)
def player3():
    s3 = 0
    timePassed3 = 0
    
    while (s3 < distance):
        s3 += random.randrange(0,3)
        print('Player 3: ' + ' ' * s3 + '>' + ' ' * (distance - s3) + '|', end = '\r')
        timePassed3 += 1
        sleep(1)
    print('\n')
    return(timePassed3, s3)

a=1

while True:
    message = input("> ")
    message = message.lower()
    if message == 'help':
        print("Start:- Race starts\nStop:- Race stops\nQuit:- Quits the program\n")
    elif message == 'start':
        distance = int(input("Enter the total distance of the race.\n> "))
    
        
        timePassed1,s1 = player1()
        timePassed2,s2 = player2()
        timePassed3,s3 = player3()
        print("Race finished!!")
        if s1 > distance:
            s1 = distance
        if s2 > distance:
            s2 = distance
        if s2 > distance:
            s2 = distance

        print(f"\n> Player 1: Distance covered = {distance} units in {timePassed1} seconds")
        print(f"\n> Player 2: Distance covered = {distance} units in {timePassed2} seconds")
        print(f"\n> Player 3: Distance covered = {distance} units in {timePassed3} seconds")
        
        if (timePassed1 < timePassed2 and timePassed1 < timePassed3):
            print("\nPlayer 1 won the race!!")
        elif (timePassed2 < timePassed1 and timePassed2 < timePassed3):
            print("\nPlayer 2 won the race!!")
        elif (timePassed3 < timePassed2 and timePassed3 < timePassed1):
            print("\nPlayer 3 won the race!!")
        elif (timePassed1 == timePassed2 and timePassed1 < timePassed3):
            print("\nPlayer 1 and Player 2 finished the race at the same time.\nBoth are winners!!")
        elif (timePassed1 == timePassed3 and timePassed1 < timePassed2):
            print("\nPlayer 1 and Player 3 finished the race at the same time.\nBoth are winners!!")
        elif (timePassed2 == timePassed3 and timePassed2 < timePassed1):
            print("\nPlayer 2 and Player 3 finished the race at the same time.\nBoth are winners!!")    
        else:
            print("\nAll players finished at the same time.\nAll are winners!!") 

    elif message == 'stop':
        print("Game stopped.. Going back to the main screen.")    
    elif message == 'quit':
        print("\nThank you for playing my game!! :D")
        break
    else:
        print("Please enter a valid command")