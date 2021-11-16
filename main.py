from player import Player
import random
import getpass
print("----RPSLS RULES----")
print("For rock: rock beats lizards, rock beats scissor. \nFor scissors: scissors beats paper, scissors beats lizard. \nFor paper: paper beats rock, paper beats Spock. \nFor lizard: lizard beats Spock, lizard beats paper. \nFor Spock: Spock beats scissors, Spock beats rock\n\n")

numPlayers = int(input("How many players will be playing? 1 or 2?"))
player1_counter = 0
player2_counter = 0
player_1 =  Player("playerone")
player_2= Player("playertwo",numPlayers)


if numPlayers == 1:
    while player1_counter < 2 and player2_counter < 2:
        print("1 for Rock, 2 for Scissors, 3 for Paper, 4 for Lizard, 5 for Spock")
        gesture_inp = int(input("Choose your gesture:"))-1
        player_1.gesture = gesture_inp
        player_2.gesture = random.randint(0,4)
        print(f'Player ones choice is: {player_1.choose_gesture()}')
        print(f'Player twos choice is: {player_2.choose_gesture()}')
        if player_1.gesture == player_2.gesture:
            continue
        elif player_1.gesture == 0 and (player_2.gesture == 1 or player_2.gesture ==3 ):
            player1_counter += 1
        elif player_1.gesture == 1 and (player_2.gesture ==2 or player_2.gesture ==3):
            player1_counter += 1
        elif player_1.gesture == 2 and (player_2.gesture ==0 or player_2.gesture ==4):
            player1_counter +=1 
        elif player_1.gesture == 3 and (player_2.gesture ==4 or player_2.gesture ==2):
            player1_counter +=1
        elif player_1.gesture == 4 and (player_2.gesture ==0 or player_2.gesture ==1):
            player1_counter +=1 
        else:
            player2_counter +=1

if numPlayers == 2:
    while player1_counter < 2 and player2_counter < 2:
        print("1 for Rock, 2 for Scissors, 3 for Paper, 4 for Lizard, 5 for Spock")
        gesture_inp = int(getpass.getpass(prompt = "Player one choose your gesture:"))-1
        player_1.gesture = gesture_inp
        gesture_inp = int(input("Player two choose your gesture:"))-1
        player_2.gesture = gesture_inp
        print(f'Player ones choice is: {player_1.choose_gesture()}')
        print(f'Player twos choice is: {player_2.choose_gesture()}')
        if player_1.gesture == player_2.gesture:
            continue
        elif player_1.gesture == 0 and (player_2.gesture == 1 or player_2.gesture ==3 ):
            player1_counter += 1
        elif player_1.gesture == 1 and (player_2.gesture ==2 or player_2.gesture ==3):
            player1_counter += 1
        elif player_1.gesture == 2 and (player_2.gesture ==0 or player_2.gesture ==4):
            player1_counter +=1 
        elif player_1.gesture == 3 and (player_2.gesture ==4 or player_2.gesture ==2):
            player1_counter +=1
        elif player_1.gesture == 4 and (player_2.gesture ==0 or player_2.gesture ==1):
            player1_counter +=1 
        else:
            player2_counter +=1

    

if player1_counter == 2:
    print("The winner is Player 1!")

elif player2_counter == 2:
    print("The winner is Player 2!")
