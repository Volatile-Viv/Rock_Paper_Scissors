import random


def intro():
    intro_print = '''
            = = = = = = = = = = ROCK, PAPER AND SCISSORS = = = = = = = = = =
        ---------------------------------------------------------------------------
        This is the project based on a very famous hand game that you may have
        played with your friends in your childhood. It is widely known as
        Rock, paper and Scissors.

        YALA YOLO !!!
        ---------------------------------------------------------------------------

        PROJECT TITLE: ROCK, PAPER AND SCISSORS
        VERSION or DATE: v1.0 , 23-01-2020
'''
    print(intro_print)


def game():
    rps = ['R', 'P', 'S']
    points = 0

    print('''
    = = = = = = = = = = = = = GAME STARTED  = = = = = = = = = = = =

    PRESS 'R' FOR ROCK
    PRESS 'P' FOR PAPER
    PRESS 'S' FOR SCISSOR

    PRESS '0' FOR EXIT
    ''')

    user = 'R'
    wish = ['Yoho', 'You are winning', 'You can beat him', 'You got 1 point', 'Nice luck']
    wish1 = ['OOPS', 'You are losing', 'This can beat you', 'You lost 1 point', 'Bad luck']
    l = random.randint(0, 4)

    while user != '0':
        user = input('Enter here -> ')
        user = user.upper()

        k = random.randint(0, 2)
        pc = rps[k]

        if user != 'R' and user != 'P' and user != 'S' and user != '0':
            print('Invalid Input !!!')

        elif user == '0':
            break

        else:
            if user == pc:
                print("Computer --> ", pc)
                print("Wow !!! Nice match with Computer")
                print("Total points --> ", points)

            elif user == 'R' and pc == 'P':
                points = points - 1
                print("Computer --> ", pc)
                print(wish1[l])
                print("Total points --> ", points)

            elif user == 'R' and pc == 'S':
                points = points + 1
                print("Computer --> ", pc)
                print(wish[l])
                print("Total points --> ", points)

            elif user == 'P' and pc == 'R':
                points = points + 1
                print("Computer --> ", pc)
                print(wish[l])
                print("Total points --> ", points)

            elif user == 'P' and pc == 'S':
                points = points - 1
                print("Computer --> ", pc)
                print(wish1[l])
                print("Total points --> ", points)

            elif user == 'S' and pc == 'R':
                points = points - 1
                print("Computer --> ", pc)
                print(wish1[l])
                print("Total points --> ", points)

            elif user == 'S' and pc == 'P':
                points = points + 1
                print("Computer --> ", pc)
                print(wish[l])
                print("Total points --> ", points)

            else:
                print('Error')
            print('\n\n')

    print("\n\nThanks for playing this game !!!")
    print('I hope you have enjoyed playing this game.')

    print("\nTotal points --> ", points)


intro()
game()

print('\n\t- Akriti and Vivek')
