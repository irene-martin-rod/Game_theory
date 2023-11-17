import random 


#Create a tuple with the game option
options = ("falcon", "pidgeon", "bourgeois")

#Add the role for bourgeois
role = ("owner", "thief")

#Create the puntuation
H = 15
P = 10
T = 0

#Create the variable round
round = 1

player_points = 0
computer_points = 0

print ("#"*20)
print ("WELCOME TO FALCON, PIDGEONS VS. BOURGEOUIS")
print ("#"*20)


#Rules of the game
while True:
    print ("*"*10)
    print ("ROUND", round)
    print ("*"*10)

    print ("TOTAL PLAYER POINTS =", player_points)
    print ("TOTAL COMPUTER POINTS =", computer_points)
    
    #Ask user's option
    player_option = input ("Falcon, pidgeon or bourgeois?")
    player_option = player_option.lower()

    if not player_option in options:
        print ("This is not a valid option")
        continue

    #Asign ramdonly the choice of the computer
    computer_option = random.choice (options)
    print ("Computer chooses ", computer_option)

    #Asign ramdonly the role of the player and the computer
    player_role = random.choice (role)

    if player_option == "falcon":
        if computer_option == "falcon":
            print ("Falcon vs. falcon")
            player_points_round = (P - H)/2
            computer_points_round = (P - H)/2
            print ("Draw")
            print ("ROUND PLAYER POINTS = ", player_points_round)
            print ("ROUND COMPUTER POINTS = ", computer_points_round)
            player_points = player_points + player_points_round
            computer_points =computer_points + computer_points_round
        elif computer_option == "pidgeon":
            print ("Falcon vs. pidgeon")
            print ("Falcon wins pidgeon")
            player_points_round = P
            computer_points_round = 0
            print ("Player wins this round")
            print ("ROUND PLAYER POINTS = ", player_points_round)
            print ("ROUND COMPUTER POINTS =", computer_points_round)
            player_points = player_points + player_points_round
            computer_points =computer_points + computer_points_round
        elif computer_option == "bourgeois":
            print ("Falcon vs. bourgeois")
            if player_role == "owner":
                print ("The player is the owner and the computer the thief")
                print ("The computer behaves as a pidgeon")
                player_points_round = P
                computer_points_round = 0
                print ("Player wins this round")
                print ("ROUND PLAYER POINTS = ", player_points_round)
                print ("ROUND COMPUTER POINTS = ", computer_points_round)
                player_points = player_points + player_points_round
                computer_points =computer_points + computer_points_round
            else:
                print ("The player is the thief and the computer the owner")
                print ("The computer behaves as a falcon")
                player_points_round = (P-H)/2
                computer_points_round = (P-H)/2
                print ("Draw")
                print ("ROUND PLAYER POINTS = ", player_points_round)
                print ("ROUND COMPUTER POINTS = ", computer_points_round)
                player_points = player_points + player_points_round
                computer_points =computer_points + computer_points_round
    elif player_option == "pidgeon":
        if computer_option =="falcon":
            print ("Pidgeon vs. falcon")
            print ("Falcon wins pidgeon")
            player_points_round = 0
            computer_points_round = P
            print ("Computer wins this round")
            print ("ROUND PLAYER POINTS = ", player_points_round)
            print ("ROUND COMPUTER POINTS = ", computer_points_round)
            player_points = player_points + player_points_round
            computer_points =computer_points + computer_points_round
        elif computer_option == "pidgeon":
            print ("Pidgeon.vs pidgeon")
            player_points_round = (P-2*T)/2
            computer_points_round = (P-2*T)/2
            print ("Draw")
            print ("ROUND PLAYER POINTS = ", player_points_round)
            print ("ROUND COMPUTER POINTS = ", computer_points_round)
            player_points = player_points + player_points_round
            computer_points =computer_points + computer_points_round
        elif computer_option == "bourgeois":
            print ("Pidgeon vs. bourgeois")
            if player_role == "owner":
                print ("The player is the owner and the computer the thief")
                print ("The computer behaves as a pidgeon")
                player_points_round = (P-2*T)/2
                computer_points_round = (P-2*T)/2
                print ("Draw")
                print ("ROUND PLAYER POINTS = ", player_points_round)
                print ("ROUND COMPUTER POINTS = ", computer_points_round)
                player_points = player_points + player_points_round
                computer_points =computer_points + computer_points_round
            else:
                print ("The player is the thief and the computer the owner")
                print ("Computer behaves as a falcon")
                player_points_round = 0
                computer_points_round = P
                print ("Computer wins this round")
                print ("ROUND PLAYER POINTS = ", player_points_round)
                print ("ROUND COMPUTER POINTS = ", computer_points_round)
                player_points = player_points + player_points_round
                computer_points =computer_points + computer_points_round
    elif player_option == "bourgeois":
        if computer_option == "falcon":
            print ("Bourgeois vs. falcon")
            if player_role == "owner":
                print ("The player is the owner and the computer the thief")
                print ("The player behaves as a falcon")
                player_points_round = (P-H)/2
                computer_points_round = (P-H)/2
                print ("Draw")
                print ("ROUND PLAYER POINTS = ", player_points_round)
                print ("ROUND COMPUTER POINTS = ", computer_points_round)
                player_points = player_points + player_points_round
                computer_points =computer_points + computer_points_round
            else:
                print ("The player is the thief and the computer the owner")
                print ("The player behaves as a pidgeon")
                player_points_round = 0
                computer_points_round = P
                print ("Computer wins this round")
                print ("ROUND PLAYER POINTS = ", player_points_round)
                print ("ROUND COMPUTER POINTS = ", computer_points_round)
                player_points = player_points + player_points_round
                omputer_points =computer_points + computer_points_round
        elif computer_option == "pidgeon":
            print ("Bourgeois vs. pidgeon")
            if player_role == "owner":
                print ("The player is the owner and the computer the thief")
                print ("The player behaves as a falcon")
                player_points_round = P
                computer_points_round = 0
                print ("Player wins this round")
                print ("ROUND PLAYER POINTS = ", player_points_round)
                print ("ROUND COMPUTER POINTS = ", computer_points_round)
                player_points = player_points + player_points_round
                computer_points =computer_points + computer_points_round
            else:
                print ("The player is the thief and the computer the owner")
                print ("The player behaves as a pidgeon")
                player_points_round = (P-2*T)/2
                computer_points_round = (P-2*T)/2
                print ("Draw")
                print ("ROUND PLAYER POINTS = ", player_points_round)
                print ("ROUND COMPUTER POINTS = ", computer_points_round)
                player_points = player_points + player_points_round
                computer_points =computer_points + computer_points_round
        elif computer_option == "bourgeois":
            print ("Bourgeois vs. bourgeois")
            player_points_round = P/2
            computer_points_round = P/2
            print ("Draw")
            print ("ROUND PLAYER POINTS = ", player_points_round)
            print ("ROUND COMPUTER POINTS = ", computer_points_round)
            player_points = player_points + player_points_round
            computer_points =computer_points + computer_points_round
    round += 1
    
    if player_points >= 20:
        if computer_points < 20:
            print ("TOTAL PLAYER POINTS =", player_points)
            print ("TOTAL COMPUTER POINTS =", computer_points)
            print("YOU WIN!")
        elif computer_points >= 20: 
            print ("TOTAL PLAYER POINTS =", player_points)
            print ("TOTAL COMPUTER POINTS =", computer_points)
            print("DRAW")
        break
    elif computer_points >= 20:
        if player_points < 20: 
            print ("TOTAL PLAYER POINTS =", player_points)
            print ("TOTAL COMPUTER POINTS =", computer_points)
            print ("GAME OVER")
        elif player_points >= 20:
            print ("TOTAL PLAYER POINTS =", player_points)
            print ("TOTAL COMPUTER POINTS =", computer_points)
            print("DRAW")
        break
