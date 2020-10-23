# MAIN SCRIPT TO SOLVE A SUDOKU
# Santiago Garcia Arango, 2020
# Inspired by: Tech With Tim

class Sudoku:
    def __init__(self, board):
        self.board = board

    def show_board(self):
        # Go through each row (vertical)
        for i in range(len(self.board)):

            # Print horizontal dividers when needed
            if (i % 3 == 0):
                print("-------------------------")

            # Go through each column (horizontal)
            for j in range(len(self.board[0])):

                # Print vertical dividers when needed
                if (j % 3 == 0):
                    print("| ", end="")

                # Add main board and if we are in last column, jump to next row
                if j == 8:
                    print(str(self.board[i][j]) + " |")
                else:
                    print(str(self.board[i][j]) + " ", end="")
        print("-------------------------")


    def find_empty_positions(self):
        



s1 = Sudoku(
    [[7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]])

s1.show_board()

