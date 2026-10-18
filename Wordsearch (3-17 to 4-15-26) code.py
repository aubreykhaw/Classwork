import random

ROWS = 8
COLS = 8

WORDS = ["CAT", "DOG", "CODE", "PYTHON", "FISH", "TENNIS"]

EMPTY = "_"

def create_board():
    # TODO: create and return a 2D list filled with EMPTY
    board = [
        [ "_", "_", "_", "_", "_", "_", "_", "_",],
        [ "_", "_", "_", "_", "_", "_", "_", "_",],
        [ "_", "_", "_", "_", "_", "_", "_", "_",],
        [ "_", "_", "_", "_", "_", "_", "_", "_",],
        [ "_", "_", "_", "_", "_", "_", "_", "_",],
        [ "_", "_", "_", "_", "_", "_", "_", "_",],
        [ "_", "_", "_", "_", "_", "_", "_", "_",],
        [ "_", "_", "_", "_", "_", "_", "_", "_",]
    ]
    return board
    
def print_board(board):
    # TODO: print the board nicely
    print("   " + "   ".join(str(i) for i in range(ROWS)))
    for row in reversed(board):
        print(" | ".join(row))
    print()

def can_place_word(board, word, row, col, direction):
    # TODO:
    # board is a 2D list 
    # word is a string ex. "CAT" 
    # row is an integer ex. 0
    # col is an integer ex. 0 
    # direction is a string ex. "H" or "V"
    # board[row][col] is a letter or '_' 



    # could this word be placed in our board 
    # can 'CAT' be place in our board 
    # 8 rows and 8 columns 
    # what if we have 6/8 spots in our row filled -> we cannot place our word 
    # if the words overlap -> 
    # 

    # return True if the word can be placed
    # direction is "H" or "V"
    if 0>row or row>=8 or 0>col or col>=8:
        return False
    if direction == "H": 
        for i in range(len(word)): # i is the index value (int)
            if col+i < 8: 
                if board[row][col+i] != "_":
                    return False
            else:
                return False
    if direction == "V":
        for i in range(len(word)):
            if row+i < 8:
                if board[row+i][col] != "_":
                    return False
            else:
                return False
    
    return True
    
        # [ "_", "_", "_", "_", "_", "_", "_", "_",],
        # need to check if we have the length of our word amount of empty spaces together 
                



        # 
        # what would we use this i value for
        # we are using i to access each letter in our word 
    
             # letter is the acutal letter inside word 
        # do i have x consecutive spots (length of our word) open in this particular row 
        
    
            




def place_word(board, word):
    random_hor = random.randint(0,7)
    random_ver = random.randint(0,7)
    random_dir = random.choice(["H", "V"])
    while can_place_word( board, word, random_hor, random_ver, random_dir)== False:
        random_hor = random.randint(0,7)
        random_ver = random.randint(0,7)
        random_dir = random.choice(["H", "V"])
    if can_place_word( board, word, random_hor, random_ver, random_dir) == True:
        board[random_hor][random_ver] = word[0]
        if random_dir == "H":
            for i in range(len(word)):
                board[random_hor][random_ver+i] = word[i]
        if random_dir == "V":
            for i in range(len(word)):
                board[random_hor+i][random_ver] = word[i]
    
 # positions + directions until the word is placed    pass

def fill_random_letters(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "_":
                random_letter = random.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
                board[row][col] = random_letter   # replace EMPTY spots with random letters A-Z

def main():
    board = create_board()

    # TODO: place all words in WORDS onto the board
    for word in WORDS:
        place_word(board, word)

    # TODO: fill the rest of the board with random letters
    fill_random_letters(board)
    found_words = []

    while len(found_words) < len(WORDS):
        print_board(board)

        # TODO: show remaining words to find
        print ("Remaining words to find: ")
        for word in WORDS:
            if word not in found_words:
                print(word)
            

        guess = input("Enter a word: ").upper()

        # TODO:
        # if guess is correct and not already found:
        #     add to found_words
        #     print success message
        # else:
        #     print try again
        if guess in WORDS and guess not in found_words:
            found_words.append(guess)
            print("You found a word")
        else:
            print("Try again!")

    print("You found all the words!")

main()