def start():
    print("This is a Rock Paper Scissors game!")
    player_one = input("Enter your name: ")
    player_two = input("Enter your name: ")
    
    def choices(player_one_choice, player_two_choice):
        if player_one_choice == "rock" and player_two_choice == "paper":
            return ("Paper covers Rock! " + player_two + " wins!")
        elif player_one_choice == "paper" and player_two_choice == "rock":
            return ("Paper covers Rock! " + player_one + " wins!")
        elif player_one_choice == "scissors" and player_two_choice == "paper":
            return("Scissors cuts Paper! " + player_one + " wins!")
        elif player_one_choice == "rock" and player_two_choice == "scissors":
            return("Rock smashes Scissors! " + player_one + " wins!")
        elif player_one_choice == "paper" and player_two_choice == "scissors":
            return("Scissors cuts paper! " + player_two + " wins!")
        elif player_one_choice == "scissors" and player_two_choice == "rock":
            return("Rock smashes Scissors! " + player_two + " wins!")
        elif player_one_choice == player_two_choice:
            return("You tied!")
        else: 
            return("Please type rock, Paper, or Scissors!")
    
    player_one_choose = (input("Does " + player_one + " choose Rock, Paper, or Scissors? : ").lower() )
    player_two_choose = input("Does " + player_two + " choose Rock, Paper, or Scissors? : ").lower()

    print(choices(player_one_choose, player_two_choose))

    def play_Again():
        Again = input("Would you like to play the game again? ").lower()
        if Again == 'No'.lower():
            quit()
        if Again == 'Yes'.lower():
            start()
        else:
            print('Please enter Yes or No. Thank you!')
            play_Again()
    play_Again()
start()
    