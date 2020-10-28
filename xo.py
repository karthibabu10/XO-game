board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
#GAME STILL GOING
game_still_going = True

#who   win or tie
winner = None

#who turn is it
current_player = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():

    #display initial board
    display_board()

    #while game is still going
    while game_still_going:

        #handle single turn
      handle_turn(current_player)

        #check if game is going
      check_if_game_over()

        #flip to other player
      flip_player()

    # the game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie")
