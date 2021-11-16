print("----RPSLS RULES----")
print("For rock: rock beats lizards, rock beats scissor. \nFor scissors: scissors beats paper, scissors beats lizard. \nFor paper: paper beats rock, paper beats Spock. \nFor lizard: lizard beats Spock, lizard beats paper. \nFor Spock: Spock beats scissors, Spock beats rock\n\n")

numPlayers = int(input("How many players will be playing? 1 or 2?"))
player1_counter = 0
player2_counter = 0

if numPlayers == 1:
    while player1_counter < 2 or player2_counter < 2:
        print("1 for Rock, 2 for Scissors, 3 for Paper, 4 for Lizard, 5 for Spock")
        gesture_inp = int(input("Choose your gesture:"))
        

if numPlayers == 2:
    pass
    # human v human code here

if player1_counter == 2:
    print("The winner is Player 1!")

elif player2_counter == 2:
    print("The winner is Player 2!")