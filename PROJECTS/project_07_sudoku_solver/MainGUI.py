# MAIN SUDOKU SOLVER
# Santiago Garcia Arango

# REMARK --> When I have time, I will create an amazing GUI !!!!


# My other modules
import ExtractCharacteristics as EXCHAR
import MultilayerPerceptron as MyMLP
import GetSudokuBoard as GSB
import SolveSudoku as SS

s1 = GSB.GetSudokuBoard("Sudoku_R2.PNG")

solution = SS.Sudoku(s1.number_matrix, False)

print("\nSUDOKU IDENTIFICADO:\n")
solution.show_board()

solution.solve_sudoku()

print("\nSOLUCION ENCONTRADA:\n")
solution.show_board()

