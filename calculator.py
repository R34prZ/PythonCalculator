from tkinter import *

root = Tk()
root.title("Calculator")
root.configure(background="#71BCAF")
# root.geometry("240x400")
# root.maxsize(240, 400) # width x height

my_entry = Entry(root, width=34, bg="#ABAC7C")
my_entry.grid(row=0, column=0, columnspan=3, ipadx=10, ipady=10, padx=5, pady=15)

my_button1 = Button(root, padx=33, pady=30, text="1")
my_button2 = Button(root, padx=33, pady=30, text="2")
my_button3 = Button(root, padx=33, pady=30, text="3")
my_button4 = Button(root, padx=33, pady=30, text="4")
my_button5 = Button(root, padx=33, pady=30, text="5")
my_button6 = Button(root, padx=33, pady=30, text="6")
my_button7 = Button(root, padx=33, pady=30, text="7")
my_button8 = Button(root, padx=33, pady=30, text="8")
my_button9 = Button(root, padx=33, pady=30, text="9")
my_button0 = Button(root, padx=33, pady=30, text="0")

my_equalButton = Button(root, padx=71, pady=30, text="=")
my_clearButton = Button(root, padx=32, pady=71, text="C", fg="red")

my_sumButton = Button(root, padx=33, pady=30, text="+")
my_subtButton = Button(root, padx=33, pady=30, text="-")
my_multButton = Button(root, padx=33, pady=30, text="x")
my_divButton = Button(root, padx=33, pady=30, text="/")

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