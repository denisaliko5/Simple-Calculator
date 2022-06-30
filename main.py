from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("Calculator")

enter = tk.Entry(width=25, borderwidth=5, justify="right")
enter.grid(row=0, column=0, columnspan=3, padx=10, pady=10)



def button_click(number):
  current = enter.get()
  enter.delete(0, END)
  enter.insert(0, current + str(number))

def button_clear():
  enter.delete(0, END)

def button_add():
  global n1
  global math
  math = "addition"
  n1 = enter.get()
  enter.delete(0, END)

def button_subtract():
  global n1
  global math
  math = "subtraction"
  n1 = enter.get()
  enter.delete(0, END)

def button_multiply():
  global n1
  global math
  math = "multiplication"
  n1 = enter.get()
  enter.delete(0, END)

def button_divide():
  global n1
  global math
  math = "division"
  n1 = enter.get()
  enter.delete(0, END)

def button_equal():
  n2 = enter.get()
  if math == "addition":
    add = int(n1) + int(n2)
    enter.delete(0, END)
    enter.insert(0, add)
  elif math == "subtraction":
    subtract = int(n1) - int(n2)
    enter.delete(0, END)
    enter.insert(0, subtract)
  elif math == "multiplication":
    multiply = int(n1) * int(n2)
    enter.delete(0, END)
    enter.insert(0, multiply)
  elif math == "division":
    divide = int(n1) / int(n2)
    enter.delete(0, END)
    enter.insert(0, divide)

button_1 = tk.Button(text="1", padx=40, pady=20,  command=lambda:button_click(1))
button_2 = tk.Button(text="2", padx=40, pady=20,  command=lambda:button_click(2))
button_3 = tk.Button(text="3", padx=40, pady=20,  command=lambda:button_click(3))
button_4 = tk.Button(text="4", padx=40, pady=20,  command=lambda:button_click(4))
button_5 = tk.Button(text="5", padx=40, pady=20,  command=lambda:button_click(5))
button_6 = tk.Button(text="6", padx=40, pady=20,  command=lambda:button_click(6))
button_7 = tk.Button(text="7", padx=40, pady=20,  command=lambda:button_click(7))
button_8 = tk.Button(text="8", padx=40, pady=20,  command=lambda:button_click(8))
button_9 = tk.Button(text="9", padx=40, pady=20,  command=lambda:button_click(9))
button_0 = tk.Button(text="0", padx=40, pady=20,  command=lambda:button_click(0))
button_equal = tk.Button(text="=", padx=85, pady=20,  command=button_equal)
button_add = tk.Button(text="+", padx=40, pady=20,  command=button_add)
button_subtract = tk.Button(text="-", padx=40, pady=20,  command=button_subtract)
button_multiply = tk.Button(text="*", padx=40, pady=20,  command=button_multiply)
button_divide = tk.Button(text="/", padx=40, pady=20,  command=button_divide)
button_clear = tk.Button(text="CE", padx=80, pady=20,  command=button_clear)

#Positioning buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_multiply.grid(row=4, column=1)
button_divide.grid(row=4, column=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_clear.grid(row=6, column=1, columnspan=2)
window.mainloop()