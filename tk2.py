import tkinter as tk
from tkinter import messagebox
mainWindow = tk.Tk()
mainWindow.title("Calculator")

heading_label = tk.Label(mainWindow, text="First Number")
heading_label.pack()

first_number_entry= tk.Entry(mainWindow)
first_number_entry.pack()

heading_label2 = tk.Label(mainWindow, text="Second Number")
heading_label2.pack()

second_number_entry = tk.Entry(mainWindow)
second_number_entry.pack()

operations = tk.Label(mainWindow, text="Operations")
operations.pack()

def addition():
    first, second = takeValueInput()
    result = first + second
    result_label.config(text="Operations result is :"+str(result))

def subtraction():
    first, second = takeValueInput()
    result = first - second
    result_label.config(text="Operations result is :"+str(result))

def multiplication():
    first, second = takeValueInput()
    result = first * second
    result_label.config(text="Operations result is :"+str(result))

def division():
    first, second = takeValueInput()
    if second == 0:
        messagebox.showerror("Error", "Cannot divide the value by 0.")
    result = first / second
    result = round(result, 2)
    result_label.config(text="Operations result is :"+str(result))

def takeValueInput():
    first = first_number_entry.get()
    second = second_number_entry.get()

    try:
        first = int(first)
        second = int(second)

        return first, second
    except ValueError:
        if ((len(first_number_entry.get()) == 0) or (len(second_number_entry.get()) == 0)):
            messagebox.showerror("Error", "Please enter a value")
        else:
            messagebox.showerror("Error", "Enter only integer value")
        quit(0)


addition_button = tk.Button(mainWindow, text="+", command=lambda : addition())
addition_button.pack()

minus_button = tk.Button(mainWindow, text="-", command=lambda : subtraction())
minus_button.pack()

multiply_button = tk.Button(mainWindow, text="*", command=lambda : multiplication())
multiply_button.pack()

division_button = tk.Button(mainWindow, text="/", command=lambda : division())
division_button.pack()

result_label = tk.Label(mainWindow, text="Operation result is: ")
result_label.pack()

mainWindow.mainloop()
