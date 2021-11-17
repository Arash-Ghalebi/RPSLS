from ai import Ai
from human import Human
from player import Player
import random
import getpass
print("----RPSLS RULES----")
print("For rock: rock beats lizards, rock beats scissor. \nFor scissors: scissors beats paper, scissors beats lizard. \nFor paper: paper beats rock, paper beats Spock. \nFor lizard: lizard beats Spock, lizard beats paper. \nFor Spock: Spock beats scissors, Spock beats rock\n\n")

# Will determine is 2nd player is Human(Player) or Ai(Player)
numPlayers = int(input("How many players will be playing? 1 or 2? "))
# Increments by 1 for each win. First to 2 (best of 3) wins, and program terminates.
player1_counter = 0
player2_counter = 0
# Player 1 will always be Human(Player)
player_1 =  Human(input("Input Player 1 name here: "))
if numPlayers == 1:
    player_2 = Ai("Computer")
    print('\n')
    while player1_counter < 2 and player2_counter < 2:
        print("1 for Rock, 2 for Scissors, 3 for Paper, 4 for Lizard, 5 for Spock")
        # Return chosen gesture based on the number player 1 inputted/randomly generated for player 2.
        gesture1 = player_1.choose_gesture()
        gesture2 = player_2.choose_gesture()
        print(f'{player_1.name}s choice is: {gesture1}')
        print(f'Player Twos choice is: {gesture2}')
        # In case of tie, continue loop with no changes to counters.
        if gesture1 == gesture2:
            print('\n')
            continue
        # Accounts for all winning combinations based on Player 1s choice. If conditions are not met, Player 2 automatically wins.
        elif gesture1 == 'Rock' and (gesture2 == 'Scissors' or gesture2 == 'Lizard' ):
            player1_counter += 1
            print(f'{player_1.name} wins this round!\n')
        elif gesture1 == 'Scissors' and (gesture2 == 'Paper' or gesture2 == 'Lizard'):
            player1_counter += 1
            print(f'{player_1.name} wins this round!\n')
        elif gesture1 == 'Paper' and (gesture2 == 'Rock' or gesture2 == 'Spock'):
            player1_counter +=1 
            print(f'{player_1.name} wins this round!\n')
        elif gesture1 == 'Lizard' and (gesture2 == 'Spock' or gesture2 == 'Paper'):
            player1_counter +=1
            print(f'{player_1.name} wins this round!\n')
        elif gesture1 == 'Spock' and (gesture2 == 'Rock' or gesture2 == 'Scissors'):
            player1_counter +=1 
            print(f'{player_1.name} wins this round!\n')
        else:
            player2_counter +=1
            print(f'{player_2.name} wins this round!\n')
else:
    player_2 = Human(input("Input Player 2 name here: "))
    print('\n')
    while player1_counter < 2 and player2_counter < 2:
        print("1 for Rock, 2 for Scissors, 3 for Paper, 4 for Lizard, 5 for Spock")
        # In the case of a two player game, Player 1 will utilize the getpass() function in the Human(Player) class to hide their inputs from Player 2. Player 2 will input as normal.
        print("Player 1 input is hidden (no peaking Player 2!)")
        gesture1 = player_1.choose_gesture_secret()
        gesture2 = player_2.choose_gesture()
        print(f'{player_1.name}s choice is: {gesture1}')
        print(f'{player_2.name}s choice is: {gesture2}')
        if gesture1 == gesture2:
            print('\n')
            continue
        elif gesture1 == 'Rock' and (gesture2 == 'Scissors' or gesture2 == 'Lizard' ):
            player1_counter += 1
            print(f'{player_1.name} wins this round!\n')
        elif gesture1 == 'Scissors' and (gesture2 == 'Paper' or gesture2 == 'Lizard'):
            player1_counter += 1
            print(f'{player_1.name} wins this round!\n')
        elif gesture1 == 'Paper' and (gesture2 == 'Rock' or gesture2 == 'Spock'):
            player1_counter +=1 
            print(f'{player_1.name} wins this round!\n')
        elif gesture1 == 'Lizard' and (gesture2 == 'Spock' or gesture2 == 'Paper'):
            player1_counter +=1
            print(f'{player_1.name} wins this round!\n')
        elif gesture1 == 'Spock' and (gesture2 == 'Rock' or gesture2 == 'Scissors'):
            player1_counter +=1 
            print(f'{player_1.name} wins this round!\n')
        else:
            player2_counter +=1
            print(f'{player_2.name} wins this round!\n')
    

if player1_counter == 2:
    print("The winner is Player 1!")

elif player2_counter == 2:
    print("The winner is Player 2!")
