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

