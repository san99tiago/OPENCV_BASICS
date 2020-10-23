# MAIN SCRIPT TO SOLVE A SUDOKU
# Santiago Garcia Arango, 2020
# Inspired by: Tech With Tim

class Sudoku:
    def __init__(self, board, show_step_by_step):
        self.board = board
        self.show_step_by_step = show_step_by_step

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


    def find_empty_position(self):
        # Check FIRST position where the board has a zero
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return (i, j)
        
        # If there are no more empty spots, return None
        return None



    def is_valid_solution(self, number, position):
        # Check that the row is valid for Sudoku rules (not same number)
        for j in range(len(self.board[0])):
            if self.board[position[0]][j] == number and position[1] != j: 
                return False

        # Check that the column is valid for Sudoky rules (not same number)
        for i in range(len(self.board)):
            if self.board[i][position[1]] == number and position[0] != i:
                return False

        # Get specific 3x3 box of the current position checked
        box_i = position[0] // 3
        box_j = position[1] // 3

        # Check that the current 3x3 box (not same number)
        for i in range(box_i * 3, box_i * 3 + 3):
            for j in range(box_j * 3, box_j * 3 + 3):
                if self.board[i][j] == number and (i, j) != position:
                    return False

        # If all checks were ok, it means that the number is valid in position
        return True


    def solve_sudoku(self):
        # This is a recursive method approach to solve the Sudoku board...
        # We keep adding numbers to current position and recursively check...
        # if those solutions are valid, so we end up with only one solution.

        # If user wants to see each step in the solution, show board each time
        if self.show_step_by_step == True:
            self.show_board()

        # Search for empty position
        empty_position = self.find_empty_position()

        # If there are no more empty positions, it means we finished
        if not empty_position:
            return True
        else:
            current_pos = empty_position

        # Go through each possible number and check if valid (1,2,3...,7,8,9)
        for num in range(1, 10):
            if self.is_valid_solution(num, current_pos):
                # If valid solution, add current number to board
                self.board[current_pos[0]][current_pos[1]] = num

                # Try to solve new Sudoku board
                if self.solve_sudoku() == True:
                    return True

                # If it didn't work, we use backtracking to keep checking
                self.board[current_pos[0]][current_pos[1]] = 0

        # Keep returning False so the recursive method works properly
        return False



# ----------------------------TEST--------------------------------------------

s1 = Sudoku(
    [[7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]], True)

s1.show_board()
# print(s1.find_empty_position())
# print(s1.is_valid_solution(9, (0, 2)))
s1.solve_sudoku()
s1.show_board()
