import random

print("Welcome to number guess game")


def play():
    
    number = random.randint(1, 101)

    choose_mode = input("choose a mode, e for easy, h for hard: ")

    lives = 7

    if (choose_mode == 'e'):
        lives = 10
    elif (choose_mode == 'h'):
        lives = 5

    won = False

    while (lives):

        print(f"you have {lives} lives left")
        ans = int(input("guess a number between 1 and 100: \n"))
        
        if (number == ans):
            print("You got it")
            won = True
            break
        elif (number < ans):
            print("Too high")
        else:
            print("Too low")
            
        lives -= 1


    print("\n")

    if (won == False):
        print("You lose bud..")
    else:
        print("You won mate..")
        

while (True):
    play()    
    inp = input('wanna play again? (y or n)\n')
    if (inp == 'y'):
        play()
    else:
        print("See you again..")