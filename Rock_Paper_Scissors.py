# Adding a list of variants of the computer's move
import random
comp_turn = ['R', 'P', 'S']

import time

# Creating a counting list to prevent endless games
count = [0, 0]

# Player's RPS Choice
def rps_choise(t):
    if t == 'R':
        print ('Rock')
    elif t == 'P':
         print ('Paper')
    elif t == 'S':
        print ('Scissors')

# The main function of the program
def main():
    gameloop = True
    while gameloop:
        turn = input ('Take your pick:\nR - Rock, P - Paper, S - Scissors, Exit - exit\n')
        time.sleep(0.5)

# Adding the ability to interrupt a gameloop
        if turn == 'Exit':
            print('Scared to play with me? Bye')
            gameloop = False
        else:
            rps_choise(turn)
            c_turn = random.choice(comp_turn)
            rps_choise(c_turn)

# The case of a player winning
            if (turn == 'R' and c_turn == 'S') or (turn == 'P' and c_turn == 'R') or (turn == 'S' and c_turn == 'P'):
                print('Congratulations on your win! For now...')
                count[0] += 1

# The case of a computer winning
            if (turn == 'R' and c_turn == 'P') or (turn == 'P' and c_turn == 'S') or (turn == 'S' and c_turn == 'R'):
                print('You really couldn\'t beat the AI in a game that was invented thousands of years ago? It seems that humans are about to be enslaved. By who? By what... Never mind')
                count[1] += 1

# The case of a tie in the form of equal moves
            if (turn == 'R' and c_turn == 'R') or (turn == 'P' and c_turn == 'P') or (turn == 'S' and c_turn == 'S'):
                print('Were you spying on me? How could we have made the same move?!')

# Game score display to encourage interest
            print('Game score -', count[0], ':', count[1])

# Keep score and exit the cycle when reaching 10 points
            if count[0] == 10:
                print('The little human brain beat me 10 times?! I definitely need a break')
                gameloop = False
            if count[1] == 10:
                print('God, I\'m tired of humiliating you in this game - 10 of my wins already! Learn how to play and come back later')
                gameloop = False


if __name__ == '__main__':
    main()
