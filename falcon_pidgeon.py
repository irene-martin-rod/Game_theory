import random 


#Create a tuple with the game option
options = ("falcon", "pidgeon")


#Create variabes with the total points and round points of the payer and the computer
player_points = 0 
computer_points = 0
player_points_round = 0 
computer_points_round = 0

#Create a variable with the round number
round = 1


#Establish de puntuation
P = 10
H = 5
T = 2

#Create an introduction
print ("#"*20)
print ("WELCOME TO FALCON VS: PIDGEONS")
print ("#"*20)


#Rules of the game
while True:
    print ("") 
    print ("*" * 10)
    print ("ROUND", round)
    print ("*" * 10)

    print ("TOTAL PLAYER POINTS =", player_points)
    print ("TOTAL COMPUTER POINTS =", computer_points)

#Ask user's option
    player_option = input ("Falcon or pidgeon?:") 
    player_option = player_option.lower () 
    if not player_option in options:
        print ("This is not a valid option")
        continue 

#Computer's option randomly chosed
    computer_option = random.choice (options) 

#Game points:
    if player_option == "falcon":
        if computer_option == "falcon":
            print ("Falcon vs falcon")
            player_points_round = ((P-H)/2)
            computer_points_round = ((P-H)/2)
            print ("Draw")
            print ("ROUND PLAYER POINTS= ", player_points_round)
            print ("ROUND COMPUTER POINTS= ", computer_points_round)
            player_points = player_points + player_points_round #
            computer_points = computer_points + computer_points_round 

        else: 
            print == ("Falcon vs. pidgeon")
            print ("Falcon wins pidgeon")
            player_points_round = P
            print ("Player wins this round")
            print ("ROUND PLAYER POINTS= ", player_points_round)
            print ("ROUND COMPUTER POINTS= ", computer_points_round)
            player_points = player_points + player_points_round 
            computer_points = computer_points + computer_points_round 
            
    elif player_option == "pidgeon":
        if computer_option == "falcon":
            print ("Pidgeon vs. falcon")
            print ("Falcon wins pidgeon")
            computer_points_round = P
            print ("Computer wins this round")
            print ("ROUND PLAYER POINTS= ", player_points_round)
            print ("ROUND COMPUTER POINTS= ", computer_points_round)
            player_points = player_points + player_points_round 
            computer_points = computer_points + computer_points_round 
            
        else:
            print ("Pidgeon vs. pidgeon")
            player_points_round = ((P-2*T)/2)
            computer_points_round = ((P-2*T)/2)
            print ("Draw")
            print ("ROUND PLAYER POINTS= ", player_points_round)
            print ("ROUND COMPUTER POINTS= ", computer_points_round)
            player_points = player_points + player_points_round 
            computer_points = computer_points + computer_points_round 
       
    round += 1      

#Create a condition to break the loop
    if computer_points >= 20:
        if player_points < 20: 
            print ("TOTAL PLAYER POINTS =", player_points)
            print ("TOTAL COMPUTER POINTS =", computer_points)
            print ("GAME OVER")
        elif player_points >= 20:
            print ("TOTAL PLAYER POINTS =", player_points)
            print ("TOTAL COMPUTER POINTS =", computer_points)
            print("DRAW")
        break
    elif player_points >= 20:
        if computer_points < 20:
            print ("TOTAL PLAYER POINTS =", player_points)
            print ("TOTAL COMPUTER POINTS =", computer_points)
            print("YOU WIN!")
        elif computer_points >= 20: 
            print ("TOTAL PLAYER POINTS =", player_points)
            print ("TOTAL COMPUTER POINTS =", computer_points)
            print("DRAW")
        break