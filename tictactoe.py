# In this Python challenge, write a function that’ll accept two numbers. 
# These numbers will represent a position on a tic-tac-toe board. 
# They can be 0 through 8, where 0 is the top-left spot, and 8 is the bottom-right spot.
# These parameters are two marks on the tic-tac-toe board. 
# The function should return the number of the spot that can block these two spots from winning the game.

def block_win(pos1, pos2):
    # All winning combinations
    winning_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    for line in winning_lines:
        if pos1 in line and pos2 in line:
            third = [x for x in line if x != pos1 and x != pos2]
            if third:
                return third[0]
    return None
