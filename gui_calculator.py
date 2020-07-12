#   Write a GUI program to create a simple calculator
#
#
#   As an optional extra, refer to the documentation to
#   work out how to use minsize() to prevent your window
#   from being shrunk so that the widgets vanish from view. (DONE)
#
#   Hint: You may want to use the widgets .winfo_height() and
#   winfo_width() methods, in which case you should know that
#   they will not return the correct results unless the window
#   has been forced to draw the widgets by calling its .update()
#   method first.
#


try:
    import tkinter  # Python3
except ImportError:
    import Tkinter as tkinter  # Python2

# Create window
mainWindow = tkinter.Tk()
# Give title of calculator
mainWindow.title("Calculator")
# Size of the window width
mainWindow.geometry("640x480-8-200")

# setting the minimum size of the root window so widgets don't vanish from view
mainWindow.minsize(320, 240)

text_Input = tkinter.StringVar()
operator = ""
calcFrame = tkinter.Frame(mainWindow, width=300, height=700)
calcFrame.grid(row=0, column=0)


# =============================calculator========================================

def btn_click(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btn_clear_display():
    global operator
    operator = ""
    text_Input.set("")


def btn_equals_input():
    global operator
    sum_up = str(eval(operator))
    text_Input.set(sum_up)
    operator = ""


def btn_alter_display():
    global operator
    operator = ""
    if len(text_Input.get()) != 0:
        value = text_Input.get()
        text_Input.set(value[:-1])


txtDisplay = tkinter.Entry(calcFrame, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                           bg='powder red', justify='right')
txtDisplay.grid(columnspan=4)

# First row
buttonC = tkinter.Button(calcFrame, text="C", width=5, command=btn_alter_display)
buttonCE = tkinter.Button(calcFrame, text="CE", width=5, command=btn_clear_display)

# Second row
button7 = tkinter.Button(calcFrame, text="7", width=5, command=lambda: btn_click(7))
button8 = tkinter.Button(calcFrame, text="8", width=5, command=lambda: btn_click(8))
button9 = tkinter.Button(calcFrame, text="9", width=5, command=lambda: btn_click(9))
buttonPlus = tkinter.Button(calcFrame, text="+", width=5, command=lambda: btn_click("+"))

# Third row
button4 = tkinter.Button(calcFrame, text="4", width=5, command=lambda: btn_click(4))
button5 = tkinter.Button(calcFrame, text="5", width=5, command=lambda: btn_click(5))
button6 = tkinter.Button(calcFrame, text="6", width=5, command=lambda: btn_click(6))
buttonMinus = tkinter.Button(calcFrame, text="-", width=5, command=lambda: btn_click("-"))

# Fourth row
button1 = tkinter.Button(calcFrame, text="1", width=5, command=lambda: btn_click(1))
button2 = tkinter.Button(calcFrame, text="2", width=5, command=lambda: btn_click(2))
button3 = tkinter.Button(calcFrame, text="3", width=5, command=lambda: btn_click(3))
buttonMultiply = tkinter.Button(calcFrame, text="*", width=5, command=lambda: btn_click("*"))

# Fifth row
button0 = tkinter.Button(calcFrame, text="0", width=5, command=lambda: btn_click(0))
buttonEqual = tkinter.Button(calcFrame, text="=", width=5, command=btn_equals_input)
buttonDivide = tkinter.Button(calcFrame, text="/", width=5, command=lambda: btn_click("/"))

# Set up positions on the grid
buttonC.grid(row=2, column=0)
buttonCE.grid(row=2, column=1)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
buttonPlus.grid(row=3, column=3)
button4.grid(row=4, column=0)
button5.grid(row=4, column=1)
button6.grid(row=4, column=2)
buttonMinus.grid(row=4, column=3)
button1.grid(row=5, column=0)
button2.grid(row=5, column=1)
button3.grid(row=5, column=2)
buttonMultiply.grid(row=5, column=3)
button0.grid(row=6, column=0)
buttonEqual.grid(row=6, column=1)
buttonDivide.grid(row=6, column=3)

mainWindow.mainloop()
