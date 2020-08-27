# FIRST PROBLEM CHALLENGE GUI
# SANTIAGO GARCIA ARANGO

import tkinter as tk
from tkinter import ttk
import cv2 as cv
import sol_1_A
import sol_1_B
import sol_2_A
import sol_2_B
import sol_3
import sol_4
import sol_5
import sol_6_A
import sol_6_B


TITLE = "SOLUTIONS"
FONT_1 = ("Times New Roman",18,"bold")
FONT_2 = ("Times New Roman",14,"bold")


root = tk.Tk()
root.title("{} : san99tiago".format(TITLE))
root.geometry("720x540")
root.configure(bg = "black")

text_0 = tk.Label(root, text="Santiago Garcia Arango", font=FONT_1, bg="black", fg="white")
text_0.grid(row=0, column=2, columnspan=2, sticky = "ew", pady=(50,20))

text_1 = tk.Label(root, text=TITLE, font=FONT_1, bg="black", fg="yellow")
text_1.grid(row=0, column=0, columnspan=2, sticky = "ew", pady=(50,20))

# Solution 1 A
text_2 = tk.Label(root, text="Sol 1 A:", font=FONT_2, bg="black", fg="white")
text_2.grid(row=2, column=0, padx=50, pady=5)

def solution_1_A():
    sol_1_A.main()

b_1_A = ttk.Button(root, text="SOL 1 A", command=solution_1_A)
b_1_A.grid(row =2, column=1)

# Solution 1 B
text_3 = tk.Label(root, text="Sol 1 B:", font=FONT_2, bg="black", fg="white")
text_3.grid(row=3, column=0, padx=50, pady=5)

def solution_1_B():
    sol_1_B.main()

b_1_B = ttk.Button(root, text="SOL 1 B", command=solution_1_B)
b_1_B.grid(row =3, column=1)


# Solution 2 A
text_2_A = tk.Label(root, text="Sol 2 A:", font=FONT_2, bg="black", fg="white")
text_2_A.grid(row=4, column=0, padx=50, pady=5)

def solution_2_A():
    sol_2_A.main()

b_2_A = ttk.Button(root, text="SOL 2 A", command=solution_2_A)
b_2_A.grid(row=4, column=1)

# Solution 2 B
text_2_B = tk.Label(root, text="Sol 2 B:", font=FONT_2, bg="black", fg="white")
text_2_B.grid(row=5, column=0, padx=50, pady=5)

def solution_2_B():
    sol_2_B.main()
    cv.waitKey(0)
    cv.destroyAllWindows()

b_2_B = ttk.Button(root, text="SOL 2 B", command=solution_2_B)
b_2_B.grid(row=5, column=1)


# Solution 3
text_3 = tk.Label(root, text="Sol 3:", font=FONT_2, bg="black", fg="white")
text_3.grid(row=6, column=0, padx=50, pady=5, sticky="w")

def solution_3():
    sol_3.main()
    cv.waitKey(0)
    cv.destroyAllWindows()

b_3 = ttk.Button(root, text="SOL 3  ", command=solution_3)
b_3.grid(row=6, column=1)


# Solution 4
text_4 = tk.Label(root, text="Sol 4:", font=FONT_2, bg="black", fg="white")
text_4.grid(row=7, column=0, padx=50, pady=5, sticky="w")

def solution_4():
    sol_4.main()
    cv.waitKey(0)
    cv.destroyAllWindows()

b_4 = ttk.Button(root, text="SOL 4", command=solution_4)
b_4.grid(row=7, column=1)


# Solution 5
text_5 = tk.Label(root, text="Sol 5:", font=FONT_2, bg="black", fg="white")
text_5.grid(row=8, column=0, padx=50, pady=5, sticky="w")

def solution_5():
    sol_5.main()
    cv.waitKey(0)
    cv.destroyAllWindows()

b_5 = ttk.Button(root, text="SOL 5", command=solution_5)
b_5.grid(row=8, column=1)


# Solution 6 A
text_6_A = tk.Label(root, text="Sol 6 A:", font=FONT_2, bg="black", fg="white")
text_6_A.grid(row=9, column=0, padx=50, pady=5, sticky="w")

def solution_6_A():
    sol_6_A.main()
    cv.waitKey(0)
    cv.destroyAllWindows()

b_6_A = ttk.Button(root, text="SOL 6 A", command=solution_6_A)
b_6_A.grid(row=9, column=1)


# Solution 6 B
text_6_B = tk.Label(root, text="Sol 6 B:", font=FONT_2, bg="black", fg="white")
text_6_B.grid(row=10, column=0, padx=50, pady=5, sticky="w")

def solution_6_B():
    sol_6_B.main()
    cv.waitKey(0)
    cv.destroyAllWindows()

b_6_B = ttk.Button(root, text="SOL 6 B", command=solution_6_B)
b_6_B.grid(row=10, column=1)


root.mainloop()
