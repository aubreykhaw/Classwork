# =========================
# Mini Battleship Game
# =========================
import random
SIZE = 5
WATER = "~"
SHIP = "S"
HIT = "X"
MISS = "O"

def create_board():
    # Create a 5x5 board filled with WATER
    board = [
        ["~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~"]
    ]
    return board

def print_board(board):
    # Print the board with row and column numbers
    # Do NOT show ships
    print("   " + "   ".join(str(i) for i in range(SIZE)))
    for row in reversed(board):
        print(" | ".join(row))
    print()


def place_ships(board):
    # Randomly place 3 ships on the board

    # Need to store the coordinates of 3 ships somewhere and return these stored coordinates
    ships = []
    while len(ships) < 3:
        ranrow = random.randint(0,4)
        rancol = random.randint(0,4) 
        # ships is a list 
        # check if (ranrow, rancol) exists in ships 

        # ships = [(1, 1), (1, 3), (0, 3)]
        # board = [
        #     ["A", "B", "C"],
        #     ["D", "E", "F"],
        #     ["G", "H", "I"]
        # ]


        # compare random coordinates against all coordinates that are already in ships
        
        if ships == []:
            ships.append((ranrow, rancol))       
        placed = False
        for column in range(len(ships)):
            if ships[column] == (ranrow,rancol):
                placed = True
        if placed == False:
            ships.append((ranrow, rancol))
    return ships
    
    

def is_valid_guess(board, r, c):
    # Check bounds  
    # if the spot was already guessed
    if 0>r or r>=5 or 0>c or c>=5:
        return False
    guessed = False

 
    if board[r][c] == HIT or board[r][c] == MISS: 
        guessed = True
        print("Spot already guessed.")
        return False
    if not guessed:
        return True


    # if spot is already guessed  
     

def make_guess(board, ships, r, c):
    # Update board based on hit or miss
    # Return True if hit, False otherwise
    if (r,c) in ships:
        board[r][c] = HIT
        ships.remove((r,c))
        return True
    else:
        board[r][c] = MISS
        return False
    
    
def all_ships_sunk(ships):
    # Return True if all ships are hit
    if ships == []:
        return True
    else:
        return False

def play_game():
    board = create_board()
    ships = place_ships(board)

    print("Welcome to Battleship!")
    print_board(board)

    while not all_ships_sunk(ships):
        r = int(input("Row (0-4): "))
        c = int(input("Col (0-4): "))

        if not is_valid_guess(board, r, c):
            print("Invalid guess. Try again.")
            continue

        hit = make_guess(board, ships, r, c)
        if hit:
            print("HIT!")
        else:
            print("MISS!")

        print_board(board)

    print("You sunk all the ships!")

play_game()