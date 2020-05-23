import random
import os

# Function to display board
def display_board(board):
    os.system('cls')
    print("   " + "|" + "   " + "|" + "   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print("   " + "|" + "   " + "|" + "   ")
    print("-----------")
    print("   " + "|" + "   " + "|" + "   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("   " + "|" + "   " + "|" + "   ")
    print("-----------")
    print("   " + "|" + "   " + "|" + "   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("   " + "|" + "   " + "|" + "   ")

# Function to accept player input
def player_input() :
    '''
    Function to accept player input, output in the form (Player1_marker,Player2_marker).
    '''
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1: Choose X or O : ").upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

# Function to toss for who will get the first chance
def choose_first() : 
    if random.randint(0,1) == 0:
        return "Player 1"
    else :
        return "Player 2"

# Function to accept the position from player where he wishes to put a mark
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))
    return position

# Function to check whether the chosen board position is empty or not
def space_check(board,position) :
    return board[position] == " "

# Function to place the mark on board
def place_marker(board,marker,position):
    board[position] = marker

# Function to check if the board is full or not
def full_board_check(board) :
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

# Function to check whether a move leads to win or not
def win_check(board,marker):
    '''
    Returns a boolean according to winning status of a player
    '''
    return ((board[1] == marker and board[2] == marker and board[3] ==  marker) or 
    (board[4] == marker and board[5] == marker and board[6] ==  marker) or 
    (board[7] == marker and board[8] == marker and board[9] ==  marker) or
    (board[1] == marker and board[4] == marker and board[7] ==  marker) or 
    (board[2] == marker and board[5] == marker and board[8] ==  marker) or 
    (board[3] == marker and board[6] == marker and board[9] ==  marker) or 
    (board[1] == marker and board[5] == marker and board[9] ==  marker) or
    (board[3] == marker and board[5] == marker and board[7] ==  marker))

# Function to ask the player if the want to play again (returns a boolean)
def replay():
    choice = input("Play again? Enter Y or N.").upper()
    return choice == "Y"

# Main logic for game

print("Welcome to TIC TAC TOE!")

while True :

    # Creating a new game board
    game_board = [" "]*10

    # Assigning the markers
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn + " will play first.")

    play_game = input("Ready to play? Y or N : ").upper()

    if play_game == "Y":
        game_on = True
    else:
        game_on = False

    # Beginning the game
    while game_on:
        if turn == "Player 1":
            display_board(game_board)
            print("Player 1's turn.")
            position = player_choice(game_board)
            place_marker(game_board,player1_marker,position)

            if win_check(game_board,player1_marker):
                display_board(game_board)
                print("Player 1 wins!!")
                game_on = False
            else :
                if full_board_check(game_board):
                    display_board(game_board)
                    print("Draw!!")
                    break
                else:
                    turn = "Player 2"

        elif turn == "Player 2":
            display_board(game_board)
            print("Player 2's turn.")
            position = player_choice(game_board)
            place_marker(game_board,player2_marker,position)

            if win_check(game_board,player2_marker):
                display_board(game_board)
                print("Player 2 wins!!")
                game_on = False
            else :
                if full_board_check(game_board):
                    display_board(game_board)
                    print("Draw!!")
                    break
                else:
                    turn = "Player 1" 
                
    if not replay():
        print("Goodbye!")
        break
