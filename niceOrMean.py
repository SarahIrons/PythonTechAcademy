##Python: 3.12.0
##Author: Sarah Irons
##Purpose: The Tech Academy Sofware Developer BootCamp Course: This game's goal is to teach/demonstrate how
## to pass variables from function to function while producing a working game.

##Imported colorama to add colorful text and background. 

from colorama import Back, Fore
print(Back.CYAN + 'Get ready to play a game!')
print(Fore.MAGENTA)

def start(nice=0, mean=0, name="") :
#get user's name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)

def describe_game(name) :
    """check if this is new game or not.
if it is new, get user's name. if not, thank player for playing again.
this means:
if we do not have player name we need to get it
"""
    if name !="":
        print("\nThank you for playing again,  {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name?\n>>>").capitalize()
                if name !="":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop=False

    return name


def nice_mean(nice,mean,name) :
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a conversation. Will you be nice \nor mean? (N/M) \n>>>:  ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling.")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off.")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #pass the three variables to the score ()


def show_score(nice,mean,name) :
    print("\n{}, your current total:\n {},( Nice) and {}, Mean)".format(name,nice,mean))

def score (nice,mean,name) :
    #score function is being passed the values stored within the three variables
    if nice >2: #if cond is valid will call win function
        win(nice,mean,name)
    if mean>2: #if cond is valid call lose function passing in the variables so it can use them
            lose(nice,mean,name)
    else: # else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)

def win(nice,mean,name) :
    #substitute the wildcards with our variable values
    print("\nNice job {}, you win! \nEveryone loves you and you've\nmade loads of friends along the way!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)

def lose(nice,mean,name) :
    #substitute the {} wildcards with our variable values
    print("\nAhh this is delulu! Game over!{}, you will live alone in a wretched van by the river.".format(name))
    #call again function and pass in our variables
    again(nice,mean,name) 

def again (nice,mean,name) :
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n): \n>>>".lower())
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            stop = False
            print("Ok! Sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter (Y) for 'YES', (N) for 'NO': \n>>>")

def reset (nice,mean,name) :
    nice = 0
    mean = 0
    #notice that the name variable is not reset if that same user elects to play again.
    start(nice,mean,name)
    




if __name__=="__main__":
    start()
