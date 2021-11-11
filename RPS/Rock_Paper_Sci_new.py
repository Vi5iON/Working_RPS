''' 
Table for game results.
-----------------------

 (y)computer |   rock(r)    paper(p)   scissor(s)
user(x)      |
--------------------------------------------------
rock(r)      |   rr         rp         rs
             |              l          w
--------------------------------------------------
paper(p)     |   pr         pp         ps
             |   w                     l
--------------------------------------------------
scissor(s)   |   sr         sp         ss
             |   l          w
--------------------------------------------------

Wins and losses with repect to user.

'''

import random, time, start, os, end_game

"""
as per game rules user and computer select any one of these three.
"""
possibilities = {
    'rock': 'r',
    'paper': 'p',
    'scissor': 's'
}

# these are user winning senarios
win = {
    'rs': 'Rock smashes scissor. You win!!',
    'pr': 'Paper covers rock. You win!!',
    'sp': 'Scissor cuts paper. You win!!'
}

# these are computer winning senarios or user loosing senarios
loss = {
    'rp': 'Rock gets covered by paper. Computer wins!!',
    'ps': 'Paper is cut by scissor. Computer wins!!',
    'sr': 'Scissor is smashed by rock. Computer wins!!'
}
# if it doesn't fall in any of these senarios then they chose the same

class Score:
    user_score = 0
    comp_score = 0

scr = Score()

#start the program
def main():
    global scr
    start.main()
    time.sleep(1)
    os.system('cls')
    game()
    while True:
        #creates a loop to keep the game running
        want = read('Do you want to play again? (y/n)\n')
        if want.lower() == 'y':
            os.system('cls')
            game()
        else :
            #quitung the game
            os.system('cls')
            print(f'\n\n\n\n\t\t\tYour score {scr.user_score} and computers score {scr.comp_score}')
            if scr.user_score > scr.comp_score :
                print(f'\t\t\tYou won.\n')
            elif scr.user_score < scr.comp_score :
                print(f'\t\t\tComputer won.\n')
            else :
                print(f'\t\t\tIt\'s a draw.\n')
            time.sleep(2)
            end_game.main()
            break

#this is the main function that starts the game
def game():
    print(f'!!!!!!!!!!!!!! Rock, Paper or Scissor !!!!!!!!!!!!!!\n\nUser score: {scr.user_score}\tComputer score: {scr.comp_score}\n')
    x_key = possibilities.get(user_turn(), 0)
    if x_key :
        start_time = time.time()
        y_key = possibilities.get(comp_turn())
        result(x_key+y_key)
        print(f'\n\nTime of execution {time.time() - start_time}')
    else :
        print('!! Invalid input !!')


#this function takes care of user choosing
def user_turn()->str:
    print('Your turn.\n-----------')
    user_input = read('Type Rock, Paper or Scissor to pick.\n')
    print(f'\nYou have picked {user_input.lower()}.\n')
    return user_input.lower()


#this function takes care of computer choosing using random.choice()
#here we convert dict to list for random to navigate
def comp_turn()->str:
    print('Computer\'s turn.\n----------------')
    print('Computer is choosing between rock, paper and scissor.')
    comp_input = random.choice(list(possibilities))
    print(f'Computer has picked {comp_input.lower()}.\n')
    return comp_input.lower()


#based on user selection and computers selection this block decides the winner
def result(x:str):
    global scr
    if win.get(x, 'none') != 'none' :
        print(win.get(x))
        scr.user_score += 1
    elif loss.get(x, 'none') != 'none' :
        print(loss.get(x))
        scr.comp_score += 1
    else :
        print('Draw!! Both are the same.')


#this is used to read data from user
def read(msg: str)->str:
    return input(msg)


# keep the game running in a loop
if __name__ == '__main__' :
    main()