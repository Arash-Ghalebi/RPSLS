from ai import Ai
from human import Human
from player import Player
import random
import getpass
print("----RPSLS RULES----")
print("For rock: rock beats lizards, rock beats scissor. \nFor scissors: scissors beats paper, scissors beats lizard. \nFor paper: paper beats rock, paper beats Spock. \nFor lizard: lizard beats Spock, lizard beats paper. \nFor Spock: Spock beats scissors, Spock beats rock\n\n")

numPlayers = int(input("How many players will be playing? 1 or 2?"))
player1_counter = 0
player2_counter = 0
player_1 =  Human(input("Input Player 1 name here: "))
if numPlayers == 1:
    player_2 = Ai("Computer")
    while player1_counter < 2 and player2_counter < 2:
        print("1 for Rock, 2 for Scissors, 3 for Paper, 4 for Lizard, 5 for Spock")
        gesture1 = player_1.choose_gesture()
        gesture2 = player_2.choose_gesture()
        print(f'{player_1.name}s choice is: {gesture1}')
        print(f'Player twos choice is: {gesture2}')
        if gesture1 == gesture2:
            continue
        elif gesture1 == 'Rock' and (gesture2 == 'Scissors' or gesture2 == 'Lizard' ):
            player1_counter += 1
        elif gesture1 == 'Scissors' and (gesture2 == 'Paper' or gesture2 == 'Lizard'):
            player1_counter += 1
        elif gesture1 == 'Paper' and (gesture2 == 'Rock' or gesture2 == 'Spock'):
            player1_counter +=1 
        elif gesture1 == 'Lizard' and (gesture2 == 'Spock' or gesture2 == 'Paper'):
            player1_counter +=1
        elif gesture1 == 'Spock' and (gesture2 == 'Rock' or gesture2 == 'Scissors'):
            player1_counter +=1 
        else:
            player2_counter +=1
else:
    player_2 = Human(input("Input Player 2 name here: "))
    while player1_counter < 2 and player2_counter < 2:
        print("1 for Rock, 2 for Scissors, 3 for Paper, 4 for Lizard, 5 for Spock")
        gesture1 = player_1.choose_gesture()
        gesture2 = player_2.choose_gesture()
        print(f'{player_1.name}s choice is: {gesture1}')
        print(f'{player_2.name}s choice is: {gesture2}')
        if gesture1 == gesture2:
            continue
        elif gesture1 == 'Rock' and (gesture2 == 'Scissors' or gesture2 == 'Lizard' ):
            player1_counter += 1
        elif gesture1 == 'Scissors' and (gesture2 == 'Paper' or gesture2 == 'Lizard'):
            player1_counter += 1
        elif gesture1 == 'Paper' and (gesture2 == 'Rock' or gesture2 == 'Spock'):
            player1_counter +=1 
        elif gesture1 == 'Lizard' and (gesture2 == 'Spock' or gesture2 == 'Paper'):
            player1_counter +=1
        elif gesture1 == 'Spock' and (gesture2 == 'Rock' or gesture2 == 'Scissors'):
            player1_counter +=1 
        else:
            player2_counter +=1
    

if player1_counter == 2:
    print("The winner is Player 1!")

elif player2_counter == 2:
    print("The winner is Player 2!")
