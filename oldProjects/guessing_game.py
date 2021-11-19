from random import * 

random_num = randint(1,10)

def game():
    user_guess = input("Guess the number I am thinking of between 1 and 10! ")
    if user_guess == str(random_num):
        print("You win!!!")
    else:
        print("Nope. Guess again..")
        game() #this is a recursive function can be considered a loop inside your function or just a function that calles itself, like so above


print(" ")

game()






