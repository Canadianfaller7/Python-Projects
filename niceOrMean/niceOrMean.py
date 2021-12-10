#
# Python 3.10
#
# Author: Spencer Merrill
#
# Purpose: The tech academy - python course, creating our first program together.
#          Demonstrating how to pass variables from function to function while
#          producing a functional game.
#
#          Remember, function_name(varable) _means that we pass in the variable.
#          return variable _ means that we are teturning the varble back to the calling function.
#

#from playsound import playsound



def start(nice = 0, mean = 0, name = ""):
    # get users name
    name = describeGame(name)
    nice,mean,name = niceMean(nice,mean,name)


def describeGame(name):
    """
        check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thnak the player for
        playing again and continue with the game
    """
    # meaning, if we do not already have this ser's name,
    # then they are a new player and we need to get their name

    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name


def niceMean(nice, mean, name):
    # by making stop equal to True we can use it in our while loop to run our code inside the loop and then when we
    # want the loop to stop, then we equal stop to False
    stop = True
    while stop:
        showScore(nice, mean, name)
        print("\nA stranger stranger approches you for a conversation.")
        pick = input("\nThe stranger asks you a question about what you do? \nThey are interested in knowing in\nknowing what you do.\nWill you be nice or Mean while answering their question? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...\nturns around and says 'I am a hiring manager \nand I want you to come \nwork for my company as a programmer!'")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...\nand says 'You made a huge mistake kid.'")
            mean = (mean + 1)
            stop = False
    score(nice, mean, name) # pass the 3 bariables to the score()


def showScore(nice, mean, name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name, nice, mean))


def score(nice, mean, name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: # if condition is valid, call win function passing in the variables so it can use them
        #playsound('winGame.mp3')
        win(nice, mean, name)
    if mean > 2: # if condition is valid, call the lose function passing in the variables so it can use them
        #playsound('lose.wav')
        lose(nice, mean, name)
    else:        # else, call niceMean function passing in the variables so it can use them
        niceMean(nice, mean, name)


def win(nice, mean, name):
    # Substitue the {} wildcards with our variable values
    print("\nNice job {}, you win! \nEveryone loves you and you've made lots of friends along the way!".format(name))
    # call again function and pass in our vairables
    again(nice, mean, name)

def lose(nice, mean, name):
     # Substitue the {} wildcards with our variable values
    print("\nAhhh too bad {}, game over! \nYou live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    # call again function and pass in our vairables
    again(nice, mean, name)

def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (Y/N): \n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', or ( N ) for 'NO': \n>>> ")


def reset(nice, mean, name):
    nice = 0
    mean = 0
    # notice, I do not reset the name variable as that same user has elected to play again
    start(nice, mean, name)



if __name__ == "__main__":
    start()
