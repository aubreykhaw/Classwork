
# Connect Four Game

# Constants
ROWS = 6
COLS = 7
EMPTY = "_"
PLAYER1 = "X"
PLAYER2 = "O"

# Function to create the board
def create_board():
    # Create a 6x7 grid filled with the EMPTY value
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

# Function to print the board
def print_board(board):
    print("   " + "   ".join(str(i) for i in range(COLS)))
    for row in reversed(board):
        print(" | ".join(row))
    print()

# Function to drop a piece into the board
def drop_piece(board, row, col, piece):
    # Fill the board at the given row and column with the piece (X or O)
    board[row][col] = piece

# Function to check if a column is full
def is_valid_column(board, col):
    # Check if the top row in the selected column is EMPTY
    return board[5][col] == "_"

# Function to get the next available row in a column
def get_next_open_row(board, col):
    # Loop from bottom to top of the column and find the first empty spot
    for row in range(ROWS): # for each row, within 0 to 6 
        if board[row][col] == EMPTY:
            return row

# Function to check if a player has won
def check_win(board, piece):
    # Horizontal, vertical, and diagonal checks for a win will go her   e
    
    for row in range(ROWS):
        for col in range(4):
            if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                return True 

    for row in range(4):
        for col in range(COLS):
            if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                return True 

    for row in range(3):
        for col in range(4):
            if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                return True
            
    for row in range(3,6):
        for col in range(4):
            if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece and board[row-3][col+3] == piece:
                return True
# Main game function
def play_game():
    # Step 1: Create the board if
    board = create_board()

    # Step 2: Set game_over to False and turn to 0
    game_over = False
    turn = 0

    # Step 3: Print the initial empty board
    print_board(board)

    # Step 4: Main game loop
    while not game_over:
        # Step 5: Decide which player's turn it is
        if turn % 2 == 0:
            print("Player 1's turn (X)")
            col = int(input("Choose a column (0-6): "))  # Ask Player 1 for input
            piece = PLAYER1
        else:
            print("Player 2's turn (O)")
            col = int(input("Choose a column (0-6): "))  # Ask Player 2 for input
            piece = PLAYER2

        # Step 6: Check if the selected column is valid and make the move
        if is_valid_column(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, piece)

            # Step 7: Print the updated board
            print_board(board)

            # Step 8: Check if the current player has won
            if check_win(board, piece):
                print("Player {turn % 2 + 1} wins!")
                game_over = True
        else:
            print("Column is full. Try another one.")

        # Step 9: Change turns
        turn += 1

# Start the game
play_game()

       
