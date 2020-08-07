import string
import random

board_array = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

def genrate_board():
    print(board_array[1]+'|'+board_array[2]+'|'+board_array[3])
    print('-'+'--'+'--')
    print(board_array[4]+'|'+board_array[5]+'|'+board_array[6])
    print('-'+'--'+'--')
    print(board_array[7]+'|'+board_array[8]+'|'+board_array[9])
    
def play_game():
    count = 0
    state = 'X'
    valcheck = []
    while(count < 9):
        
        board_val = int(input(f'Enter cell no {state}:'))
        if board_val not in valcheck and board_val in range(1,10):
            valcheck.append(board_val)
            global board_array
            board_array[board_val] = state
            count +=1
            print(valcheck)
            if board_array[1] == board_array[2] == board_array[3] == state:
                print(f'{state} has won')
                genrate_board()
                break
            elif board_array[4] == board_array[5] == board_array[6] == state:
                print(f'{state} has won')
                genrate_board()
                break
            elif board_array[7] == board_array[8] == board_array[9] == state: 
                print(f'{state} has won')
                genrate_board()
                break
            elif board_array[1] == board_array[4] == board_array[7] == state: 
                print(f'{state} has won')
                genrate_board()
                break
            elif board_array[2] == board_array[5] == board_array[8] == state: 
                print(f'{state} has won')
                genrate_board()
                break
            elif board_array[3] == board_array[6] == board_array[9] == state:
                print(f'{state} has won')
                genrate_board()
                break
            elif board_array[1] == board_array[5] == board_array[9] == state: 
                print(f'{state} has won')
                genrate_board()
                break
            elif board_array[3] == board_array[5] == board_array[7] == state:
                print(f'{state} has won')
                genrate_board()
                break
            
            genrate_board()
            
            if state == 'X':
                state = 'O'
            else:
                state = 'X'
        else:
            print('Enter valid number')
        if count == 9:
            print('Game over and its a draw')
            restart = str(input('do u wanna play again (y/n)')).lower()
            if restart == 'y':
                startup_play()
            else:
                break
        #print(board_array) 
    pass


def startup_play():
    print('press head(H) or tail(T)')
    toss = str(input())
    if toss.lower() == 't' or toss.lower() == 'h':
        genrate_board()
        u1 = ''
        u2 = ''
        toss_rand = random.choice('ht')
        if toss == toss_rand:
            #user 1
            print('user 1 won')
            u1 = 'X'
            u2 = 'O'
        else:
            # user 2
            print('user 2 won')
            u2 = 'X'
            u1 = 'O'
        print(f'user1 = {u1}, user2 = {u2}')
        play_game()

    else:
        print('enter valid input')
        startup_play()

if __name__ == "__main__":
    startup_play()