import random #import the library that allows to assign ramdonly


#Create a tuple with the game option
options = ("falcon", "pidgeon")


#Create two variabes with the point of the payer and the computer
player_points = 0 #the toatal puntuation
computer_points = 0
player_points_round = 0 #the puntuation of each round
computer_points_round = 0

#Create a variable with the round number
round = 1

#We have to create a loop to repit all the process until a player wins 50 points. And in each round, we hace to obtain a puntuation and acummulate to the previous points
#Establish de puntuation
P = 10
H = 5
T = 2

#Create an introduction
print ("#"*20)
print ("WELCOME TO FALCON VS: PIDGEONS")
print ("#"*20)

print ("Dileme proposed by John Maynard Smith. This dileme try to explain how individuals within a population behave when they compete by resources and which conduct is the most estable evolutionary strategy or which is the most stable prportion. Falcon individuals are aggressive whereas pidgeons always dialogue. Falcons fight to obtain the resource, although this can cause some damage. Pidgeons try to persude to obtain the resource and if they don't win, they retire and only lose time.\n Therefore, the game have these variables:\n- P: benefit of wining the prey (resource)\n- H: the cost of being damage\n- T: losed time in an argument without fight.\n\nIn this case, we are going to consider these rules are:\n- P > H\n- P > T\n- H > T\n- Falcon vs. falcon: there will we a fight. The winner obtain the prey without damage (P), but the loser will suffer harm (-H).\n\nTherefore, the average benefit per\n- Falcon is (P-H)/2\n- Falcon vs. pidgeon: the falcon obtains the prey (P), and the pidgeon doesn't have or benefit or loses (0)|n- Pidgeon vs. pidgeon: they try to dialogue. The winner obtains the prey but aldo he has lost time (P-T). The looser has lost time (-T). The average benefit per pidgeon is (P-2T)/2)")


#Now we stablish the rules of the play
while True:
    print ("") #dejar una línea en blanco
    print ("*" * 10)
    print ("ROUND", round)
    print ("*" * 10)

    print ("TOTAL PLAYER POINTS =", player_points)
    print ("TOTAL COMPUTER POINTS =", computer_points)

    player_option = input ("Falcon or pidgeon?:") ##Create a input to ask the player which option want to choose
    player_option = player_option.lower () #convert all the letter in lowercase letters
    if not player_option in options:
        print ("This is not a valid option")
        continue #para que no cuente la ronda y sume uno

    computer_option = random.choice (options) #Create a variable with the computer choice, obtained in a random way

    if player_option == "falcon":
        if computer_option == "falcon":
            print ("Falcon vs falcon")
            player_points_round = ((P-H)/2)
            computer_points_round = ((P-H)/2)
            print ("Draw")
            print ("ROUND PLAYER POINTS= ", player_points_round)
            print ("ROUND COMPUTER POINTS= ", computer_points_round)
            player_points = player_points + player_points_round #en aech loop, we sobrescribe the value with the sum of the round before
            computer_points = computer_points + computer_points_round 

        else: #we don't have to specify the options because there is not more option than pidgeon
            print == ("Falcon vs. pidgeon")
            print ("Falcon wins pidgeon")
            player_points_round = P
            print ("Player wins this round")
            print ("ROUND PLAYER POINTS= ", player_points_round)
            print ("ROUND COMPUTER POINTS= ", computer_points_round)
            player_points = player_points + player_points_round #en aech loop, we sobrescribe the value with the sum of the round before
            computer_points = computer_points + computer_points_round 
            
    elif player_option == "pidgeon":
        if computer_option == "falcon":
            print ("Pidgeon vs. falcon")
            print ("Falcon wins pidgeon")
            computer_points_round = P
            print ("Computer wins this round")
            print ("ROUND PLAYER POINTS= ", player_points_round)
            print ("ROUND COMPUTER POINTS= ", computer_points_round)
            player_points = player_points + player_points_round #en aech loop, we sobrescribe the value with the sum of the round before
            computer_points = computer_points + computer_points_round 
            
        else:
            print ("Pidgeon vs. pidgeon")
            player_points_round = ((P-2*T)/2)
            computer_points_round = ((P-2*T)/2)
            print ("Draw")
            print ("ROUND PLAYER POINTS= ", player_points_round)
            print ("ROUND COMPUTER POINTS= ", computer_points_round)
            player_points = player_points + player_points_round #en aech loop, we sobrescribe the value with the sum of the round before
            computer_points = computer_points + computer_points_round 
       
    round += 1 #plus one to the round       

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