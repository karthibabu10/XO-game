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

# handle single turn of arbitrary player
def handle_turn(player):

  print(player+"'s turn.")

  position = input("Choose a position from 1 to 9")

  valid = False
  while not valid:

    while position not in ["1", "2", "3", "4", "5", "6","7", "8", "9"]:
      position = input("Invalid input. Choose a position from 1 to 9")


    position = int(position) - 1
    if board[position] == "-":
      valid = True
    else:
      print("You cant go there . Go again")

  board[position] = player
  display_board()


def check_if_game_over():
    check_for_win()
    check_for_tie()
