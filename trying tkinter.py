from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")



root = Tk()
root.title("Ezzo Calculator")
root.geometry("240x375")
equation = StringVar()

display = Entry(root, textvariable=equation)
display.grid(column=0, row=0, columnspan=6)

AC = Button(root, text="AC", height=2, width=6, command=clear, bg="#ba2929", fg="white")
AC.grid(column=0, row=1)

seven = Button(root, text=7, height=4, width=6, command=lambda: press(7), bg="#95a1ab", fg="white")
seven.grid(column=0, row=2)

eight = Button(root, text=8, height=4, width=6, command=lambda: press(8), bg="#95a1ab", fg="white")
eight.grid(column=1, row=2)

nine = Button(root, text=9, height=4, width=6, command=lambda: press(9), bg="#95a1ab", fg="white")
nine.grid(column=2, row=2)

four = Button(root, text=4, height=4, width=6, command=lambda: press(4), bg="#95a1ab", fg="white")
four.grid(column=0, row=3)

five = Button(root, text=5, height=4, width=6, command=lambda: press(5), bg="#95a1ab", fg="white")
five.grid(column=1, row=3)

six = Button(root, text=6, height=4, width=6, command=lambda: press(6), bg="#95a1ab", fg="white")
six.grid(column=2, row=3)

one = Button(root, text=1, height=4, width=6, command=lambda: press(1), bg="#95a1ab", fg="white")
one.grid(column=0, row=4)

two = Button(root, text=2, height=4, width=6, command=lambda: press(2), bg="#95a1ab", fg="white")
two.grid(column=1, row=4)

three = Button(root, text=3, height=4, width=6, command=lambda: press(3), bg="#95a1ab", fg="white")
three.grid(column=2, row=4)

zero = Button(root, text=0, height=4, width=14, command=lambda: press(0), bg="#95a1ab", fg="white")
zero.grid(column=0, row=5, columnspan=2)

dot = Button(root, text=".", height=4, width=6, command=lambda: press("."), bg="#7a7a7a", fg="white")
dot.grid(column=2, row=5)

multiply = Button(root, text="x", height=2, width=6, command=lambda: press("*"), bg="#7a7a7a", fg="white")
multiply.grid(column=2, row=1)

divide = Button(root, text="÷", height=2, width=6, command=lambda: press("/"), bg="#7a7a7a", fg="white")
divide.grid(column=1, row=1)

minus = Button(root, text="-", height=4, width=6, command=lambda: press("-"), bg="#7a7a7a", fg="white")
minus.grid(column=3, row=2)

plus = Button(root, text="+", height=4, width=6, command=lambda: press("+"), bg="#7a7a7a", fg="white")
plus.grid(column=3, row=3)

power = Button(root, text="^", height=2, width=6, command=lambda: press("**"), bg="#7a7a7a", fg="white")
power.grid(column=3, row=1)


equal = Button(root, text="=", height=9, width=6, command=equalpress, bg="#3d85c6", fg="white")
equal.grid(column=3, row=4, rowspan=2)


root.mainloop()