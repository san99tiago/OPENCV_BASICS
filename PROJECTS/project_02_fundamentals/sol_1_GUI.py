# FIRST PROBLEM CHALLENGE GUI
# SANTIAGO GARCIA ARANGO

import tkinter as tk
from tkinter import ttk
import sol_1_A
import sol_1_B


TITLE = "SOLUTIONS"
FONT_1 = ("Times New Roman",18,"bold")
FONT_2 = ("Times New Roman",14,"bold")


root = tk.Tk()
root.title("{} : san99tiago".format(TITLE))
root.geometry("600x400")
root.configure(bg = "black")

text_1 = tk.Label(root, text=TITLE, font=FONT_1, bg="black", fg="yellow")
text_1.grid(row=0, column=0, columnspan=2, sticky = "ew", pady=(50,20))

# Solution 1 A
text_2 = tk.Label(root, text="Sol 1 A:", font=FONT_2, bg="black", fg="white")
text_2.grid(row=2, column=0, padx=50, pady=10)

def solution_1_A():
    sol_1_A.main()

b_1 = ttk.Button(root, text="SOL 1 A", command=solution_1_A)
b_1.grid(row =2, column=1)

# Solution 1 B
text_3 = tk.Label(root, text="Sol 1 B:", font=FONT_2, bg="black", fg="white")
text_3.grid(row=3, column=0, padx=50, pady=10)

def solution_1_B():
    sol_1_B.main()

b_2 = ttk.Button(root, text="SOL 1 B", command=solution_1_B)
b_2.grid(row =3, column=1)

root.mainloop()
