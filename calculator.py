# icon credits -> By: benjsperry (https://icon-icons.com/icon/calculator/50442)

# importing tkinter

from tkinter import *

# setting up some configs

root = Tk()
root.title("Calculator")
root.iconbitmap("icon/calculator_icon.ico")
root.configure(background="#71BCAF")
root.geometry("240x557")
root.maxsize(240, 557) # width x height
root.minsize(240, 557)

# defining the variables, buttons, and everything for the calculator be able to work

my_entry = Entry(root, width=34, borderwidth=2, bg="#ABAC7C")
my_entry.grid(row=0, column=0, columnspan=3, ipadx=10, ipady=10, padx=5, pady=15)
 
    # this part is for the buttons functions

def resultOnClick():
    second_number = my_entry.get()
    my_entry.delete(0, END)

    if operation == "Addition":
        my_entry.insert(0, first_num + int(second_number))

    if operation == "Subtraction":
        my_entry.insert(0, first_num - int(second_number))

    if operation == "Multiplication":
        my_entry.insert(0, first_num * int(second_number))

    if operation == "Division":
        my_entry.insert(0, first_num / int(second_number))

def entry_numberOnClick(number):
    current_number = my_entry.get()
    my_entry.delete(0, END)
    my_entry.insert(0, str(current_number) + str(number))

def clearOnClick():
    my_entry.delete(0, END)

def sumOp():
    first_number = my_entry.get()
    global first_num
    global operation
    first_num = int(first_number)
    my_entry.delete(0, END)
    operation = "Addition"

def subtOp():
    first_number = my_entry.get()
    global first_num
    global operation
    first_num = int(first_number)
    my_entry.delete(0, END)
    operation = "Subtraction"

def multOp():
    first_number = my_entry.get()
    global first_num
    global operation
    first_num = int(first_number)
    my_entry.delete(0, END)
    operation = "Multiplication"

def divOp():
    first_number = my_entry.get()
    global first_num
    global operation
    first_num = int(first_number)
    my_entry.delete(0, END)
    operation = "Division"

    # this part is defining the buttons

my_button1 = Button(root, padx=33, pady=30, text="1", bg="#D7E78B", command=lambda: entry_numberOnClick(1))
my_button2 = Button(root, padx=33, pady=30, text="2", bg="#D7E78B", command=lambda: entry_numberOnClick(2))
my_button3 = Button(root, padx=33, pady=30, text="3", bg="#D7E78B", command=lambda: entry_numberOnClick(3))
my_button4 = Button(root, padx=33, pady=30, text="4", bg="#D7E78B", command=lambda: entry_numberOnClick(4))
my_button5 = Button(root, padx=33, pady=30, text="5", bg="#D7E78B", command=lambda: entry_numberOnClick(5))
my_button6 = Button(root, padx=33, pady=30, text="6", bg="#D7E78B", command=lambda: entry_numberOnClick(6))
my_button7 = Button(root, padx=33, pady=30, text="7", bg="#D7E78B", command=lambda: entry_numberOnClick(7))
my_button8 = Button(root, padx=33, pady=30, text="8", bg="#D7E78B", command=lambda: entry_numberOnClick(8))
my_button9 = Button(root, padx=33, pady=30, text="9", bg="#D7E78B", command=lambda: entry_numberOnClick(9))
my_button0 = Button(root, padx=33, pady=30, text="0", bg="#D7E78B", command=lambda: entry_numberOnClick(0))

my_equalButton = Button(root, padx=71, pady=30, text="=", bg="#C496DF", command=resultOnClick)
my_clearButton = Button(root, padx=32, pady=71, text="C", fg="red", bg="#94C1E7", command=clearOnClick)

my_sumButton = Button(root, padx=33, pady=30, text="+", bg="#EBAE67", command=sumOp)
my_subtButton = Button(root, padx=33, pady=30, text="-", bg="#EBAE67", command=subtOp)
my_multButton = Button(root, padx=33, pady=30, text="x", bg="#EBAE67", command=multOp)
my_divButton = Button(root, padx=33, pady=30, text="/", bg="#EBAE67", command=divOp)

    # this part is putting the buttons on the screen

my_button1.grid(row=3, column=0)
my_button2.grid(row=3, column=1) 
my_button3.grid(row=3, column=2) 

my_button4.grid(row=2, column=0) 
my_button5.grid(row=2, column=1) 
my_button6.grid(row=2, column=2) 

my_button7.grid(row=1, column=0) 
my_button8.grid(row=1, column=1) 
my_button9.grid(row=1, column=2)

my_button0.grid(row=4, column=0)

my_equalButton.grid(row=4, column=1, columnspan=2)
my_clearButton.grid(row=5, column=0, rowspan=2)

my_sumButton.grid(row=5, column=1)
my_subtButton.grid(row=5, column=2)
my_multButton.grid(row=6, column=1)
my_divButton.grid(row=6, column=2)

root.mainloop()