import numpy as np
import pygame
import sys

cyan = (0,255,255)
yellow = (255,255,0)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

print('\n                     WELCOME! THIS IS A CUSTOMIZABLE CONNECT FOUR GAME         \n')

#take input of name of players
player_1=input('Enter name of player 1:')
player_2=input('\nEnter name of player 2:')

#take input of keys of each player(1-9)
key_1=int(input("\nEnter the key for "+player_1+" (1-9):"))
key_2=int(input("\nEnter the key for "+player_2+" (1-9):"))

#taking input for rows and columns

ROWS=int(input("\nEnter the number of rows to play (equal to or greater than 4):"))
COLUMNS=int(input("\nEnter the number of columns to play (equal to or greater than 4):"))

pygame.font.init()

game_font = pygame.font.SysFont('arial',30,1,0)

def generate_board():
    board=np.zeros((ROWS,COLUMNS))
    #create a board with ROWSxCOLUMNS matrix(traditional connect 4)
    return board

def place_key(board,row,choice,key):#place the piece in the required position in board
    board[row][choice]=key

def check_location(board,choice):#to check if user input is valid or not in board
    return board[ROWS-1][choice] == 0 # ROWS-1 is the last row from bottom , bottom row = 0

def get_row(board,choice):#checking which row the piece falls on
    for i in range(ROWS):
        if board[i][choice] == 0:
            return i

def print_board_bottomup(board):#need to reverse it as piece fills from top
    print(np.flip(board, 0))

def check_win_horizontal(board,key):
    #checking for any winning move horizontally
    for i in range(COLUMNS-3):#cannot have win move in last three positions
        for j in range(ROWS):
            if (board[j][i]==key and board[j][i+1]==key and board[j][i+2]==key and board[j][i+3]==key):
                return True

def check_win_vertically(board,key):
    #checking for any winning move vertically
    for i in range(COLUMNS):#cannot have win move in last three positions
        for j in range(ROWS-3):
            if (board[j][i]==key and board[j+1][i]==key and board[j+2][i]==key and board[j+3][i]==key):
                return True

def check_win_rightdiagonal(board,key):
    #checking for any winning move in positive slope diagonal
    for i in range(COLUMNS-3):#cannot have win move in last three positions
        for j in range(ROWS-3):
            if (board[j][i]==key and board[j+1][i+1]==key and board[j+2][i+2]==key and board[j+3][i+3]==key):
                return True

def check_win_leftdiagonal(board,key):
    #checking for any winning move in negative slope diagonal
    for i in range(COLUMNS-3):#cannot have win move in last three positions
        for j in range(3,ROWS):#index is 3 but fourth row
            if (board[j][i]==key and board[j-1][i+1]==key and board[j-2][i+2]==key and board[j-3][i+3]==key):
                return True

def pygame_board(board,winner):
    for i in range(COLUMNS):
        for j in range(ROWS):
            #                 screen,color   [position]                    height,        width
            pygame.draw.rect(screen,cyan,(i*size_of_block,j*size_of_block,size_of_block,size_of_block))
            pygame.draw.circle(screen,yellow,(int(i*size_of_block+size_of_block//2),int(j*size_of_block+size_of_block//2)),radius)
    for i in range(COLUMNS):
        for j in range(ROWS):
            if board[j][i] == key_1:
                #                  screen,colour           [position]                                                                   radius
                pygame.draw.circle(screen,black, (int(i*size_of_block+size_of_block//2),height-int(j*size_of_block + size_of_block//2)),radius)
            elif board[j][i] == key_2:
                pygame.draw.circle(screen, white, (int(i * size_of_block + (size_of_block// 2)),height-int(j * size_of_block + size_of_block // 2)), radius)
    if game_end:#if the game ends

        screen.fill(yellow)
        text=game_font.render(winner+' IS THE WINNER!!',1,red)
        screen.blit(text,(30,height/2))
    pygame.display.update()


turns=0 #game starts with 0 turns and keeps increasing each time user inputs
winner=''#initialises winner str
game_end = 0
board=generate_board() #creates a board for user inputs
print('Welcome players!! This is the board:') #introduction
print_board_bottomup(board)
pygame.init()
size_of_block = 75
width = COLUMNS * size_of_block
height = (ROWS) * size_of_block
size = (width,height)
radius = int(size_of_block//2-10)#reducing some length to fit into the boxes
screen = pygame.display.set_mode(size)#total size of pygame window
pygame_board(board,winner)
pygame.display.update()#updates the pygame window

while not game_end:#untill the game ends

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # asking input of the first player(the column)
            if turns%2==0:
                click_position = event.pos[0]
                choice = int(click_position//size_of_block)#making it between (0-COLUMN-1)
                #choice = input("1st player select your choice from  (0 - 6):")
                #choice = int(choice)
                if check_location(board, choice):
                    row = get_row(board, choice)
                    place_key(board, row, choice, key_1)
                    # now checking all winning possibilities
                    if check_win_horizontal(board, key_1):
                        print("\n"+player_1+" IS THE WINNER!!!\n")
                        game_end = 1
                        winner = player_1

                    elif check_win_vertically(board, key_1):
                        print("\n"+player_1+" IS THE WINNER!!!\n")
                        game_end = 1
                        winner = player_1

                    elif check_win_rightdiagonal(board, key_1):
                        print("\n"+player_1+" IS THE WINNER!!!\n")
                        game_end = 1
                        winner = player_1

                    elif check_win_leftdiagonal(board, key_1):
                        print("\n"+player_1+" IS THE WINNER!!!\n")
                        game_end = 1
                        winner= player_1

                    print_board_bottomup(board)
                    pygame_board(board,winner)

            # asking input of the second player(column)
            else:
                click_position = event.pos[0]
                choice = int(click_position // size_of_block)
                #choice = int(input("2nd player select your choice from (0 - 6):"))
                if check_location(board, choice):
                    row = get_row(board, choice)
                    place_key(board, row, choice, key_2)
                    # now checking all the winning possiblities
                    if check_win_horizontal(board, key_2):
                        print("\n"+player_2+" IS THE WINNER!!!\n")
                        game_end = 1
                        winner=player_2

                    elif check_win_vertically(board,key_2):
                        print("\n" + player_2 + " IS THE WINNER!!!\n")
                        game_end = 1
                        winner = player_2

                    elif check_win_leftdiagonal(board,key_2):
                        print("\n" + player_2 + " IS THE WINNER!!!\n")
                        game_end = 1
                        winner = player_2

                    elif check_win_rightdiagonal(board,key_2):
                        print("\n" + player_2 + " IS THE WINNER!!!\n")
                        game_end = 1
                        winner = player_2

                    print_board_bottomup(board)
                    pygame_board(board,winner)
            turns = turns + 1  # increases after every move
            if game_end:
                pygame.time.wait(4000)#wait 4 seconds after winning move to return to screen














