"""
This is a simple graphical(GUI) calculator application built using Python's Tkinter library.
The calculator supports basic arithmetic operations: addition, subtraction, multiplication, and division.
 
Features:
- A user-friendly interface with buttons for digits (0-9) and operators (+, -, *, /).
- An entry field that displays the current input and results of calculations.
- The calculator allows for chaining calculations (e.g., entering "2 + 3 * 4" and pressing "=" will give the correct result).
- A clear button ("C") to reset the input field.

How to Use:
1. Click on the number buttons (0-9) to enter digits.
2. Click on the operator buttons to select the operation.
3. Click "=" to evaluate the expression and display the result.
4. Click "C" to clear the input field.

Note: The program assumes valid input and uses Python's eval() function to calculate the result of the entered expression.

Author: Himanshu Chaurasia
Date: 23-10-2024
"""

from tkinter import Tk,Entry,Button,StringVar

t = Tk()
t.title("Calculator")
t.geometry("425x280")
t.resizable(0,0)
t.configure(background="black")

a =StringVar()
def Show(c):
    a.set(a.get()+c)

def equ():
    ex=a.get()
    a.set(eval(ex))

def clr():
    a.set("")

e1 = Entry(font=("Forte",30),justify="right",textvariable=a)
e1.place(x=0,y=0,width=425,height=50)
# ROW-1 BUTTONS
b1 = Button(text="7",font=("forte",25),background="gray",foreground="white",activebackground="lightgreen",activeforeground="Black")
b1.place(x=5,y=55,width=100,height=50)
b1.configure(command=lambda:Show("7"))
b2 = Button(text="8",font=("forte",25),background="gray",foreground="white",activebackground="lightgreen",activeforeground="Black")
b2.place(x=110,y=55,width=100,height=50)
b2.configure(command=lambda:Show("8"))
b3 = Button(text="9",font=("forte",25),background="gray",foreground="white",activebackground="lightgreen",activeforeground="Black")
b3.place(x=215,y=55,width=100,height=50)
b3.configure(command=lambda:Show("9"))
b4 = Button(text="+",font=("forte",25),background="gray",foreground="white",activebackground="lightgreen",activeforeground="Black")
b4.place(x=320,y=55,width=100,height=50)
b4.configure(command=lambda:Show("+"))

# ROW-2 BUTTONS
b5 = Button(text="4",font=("forte",25),background="gray",foreground="white",activebackground="lightgreen",activeforeground="Black")
b5.place(x=5,y=110,width=100,height=50)
b5.configure(command=lambda:Show("4"))
b6 = Button(text="5",font=("forte",25),background="gray",foreground="white",activebackground="lightgreen",activeforeground="Black")
b6.place(x=110,y=110,width=100,height=50)
b6.configure(command=lambda:Show("5"))
b7 = Button(text="6",font=("forte",25),background="gray",foreground="white",activebackground="lightgreen",activeforeground="Black")
b7.place(x=215,y=110,width=100,height=50)
b7.configure(command=lambda:Show("6"))
b8 = Button(text="-",font=("forte",25),background="gray",foreground="white",activebackground="lightgreen",activeforeground="Black")
b8.place(x=320,y=110,width=100,height=50)
b8.configure(command=lambda:Show("-"))
# ROW-3 BUTTONS
b9 = Button(text="1",font=("forte",25),background="gray",foreground="white",activebackground="lightgreen",activeforeground="Black")
b9.place(x=5,y=165,width=100,height=50)
b9.configure(command=lambda:Show("1"))
b10 = Button(text="2",font=("forte",25),background="gray",foreground="white",activebackground="lightgreen",activeforeground="Black")
b10.place(x=110,y=165,width=100,height=50)
b10.configure(command=lambda:Show("2"))
b11 = Button(text="3",font=("forte",25),background="gray",foreground="white",activebackground="lightgreen",activeforeground="Black")
b11.place(x=215,y=165,width=100,height=50)
b11.configure(command=lambda:Show("3"))
b12 = Button(text="*",font=("forte",25),background="gray",foreground="white",activebackground="lightgreen",activeforeground="Black")
b12.place(x=320,y=165,width=100,height=50)
b12.configure(command=lambda:Show("*"))
# ROw-4 BUTTONS
b13 = Button(text="C",font=("forte",25),background="gray",foreground="white",activebackground="lightgreen",activeforeground="Black")
b13.place(x=5,y=220,width=100,height=50)
b13.configure(command=clr)
b14 = Button(text="0",font=("forte",25),background="gray",foreground="white",activebackground="lightgreen",activeforeground="Black")
b14.place(x=110,y=220,width=100,height=50)
b14.configure(command=lambda:Show("0"))
b15 = Button(text="=",font=("forte",25),background="gray",foreground="white",activebackground="lightgreen",activeforeground="Black")
b15.place(x=215,y=220,width=100,height=50)
b15.configure(command=equ)
b16 = Button(text="/",font=("forte",25),background="gray",foreground="white",activebackground="lightgreen",activeforeground="Black")
b16.place(x=320,y=220,width=100,height=50)
b16.configure(command=lambda:Show("/"))
t.mainloop()
