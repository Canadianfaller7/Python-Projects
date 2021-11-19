import time
name = input("Please enter the name of the person who created this game: ")
print("This game was made by " + name + "!")
time.sleep(1.5)
print("Welcome to my guessing game!")
time.sleep(1.5)
print("In this game, you will try to guess a word that I chose.")
time.sleep(1.5)
print("Good Luck!")
print('')

def start():
    player_name = input("What is your name? : ")
    time.sleep(1.5)
    print('')
    print("Greetings, " + player_name + "! It is time to guess!")
    secret_word = "Gwapo".lower()
    guesses = ''
    turns_left = 10
    while turns_left > 0:
        wrong_answer = 0
        for letter in secret_word:
            if letter in guesses:
                print(letter)
            else:
                print('_')
                wrong_answer += 1
        if wrong_answer == 0:
            print("You win! You guessed my word: " + secret_word + "!!!!")
            break
        print('')
        guess = input("Guess a letter here: ") .lower()
        guesses += guess

        if guess not in secret_word:
            turns_left -= 1
            print("Oops! This letter is not in my word. Please try again.")
            print("You have " + str(turns_left) + " more guesses left. You can do it!")
            if turns_left == 0:
                print("Game Over!")
    def play_Again():
        Again = input("Would you like to play again? yes or no? : ")
        if Again == 'No'.lower():
            quit()
        if Again == 'Yes'.lower():
            start()
        else:
            print('Please enter Yes or No. Thank you!')
    play_Again()
start()