#calculator with modern GUI 
# Add these lines at the very start of your script
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Define functions for different operations
def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    result_label.config(text=str(result))

def subtract():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 - num2
    result_label.config(text=str(result))

def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    result_label.config(text=str(result))

def divide():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    if num2 == 0:
        messagebox.showerror("Error", "Cannot divide by zero")
        return
    result = num1 / num2
    result_label.config(text=str(result))

# Create the GUI
root = tk.Tk()
root.title("Calculator | outman")
root.geometry("500x200")
root.resizable(0,0)
# Set the style of the widgets
style = ttk.Style()
style.configure("TButton", padding=5, font=("Segoe UI", 16))
style.configure("TEntry", padding=5, font=("Segoe UI", 16))
style.configure("TLabel", font=("Segoe UI", 12))

# Add some animations
def animate():
    for i in range(10):
        root.update()
        root.after(50)

# Show a welcome message
welcome_label = ttk.Label(root, text=" Welcome to my calculator app", style="TLabel" , font=("segeoe UI", 12))
welcome_label.pack(pady=20)
animate()

# Add the input fields for the numbers
entry1 = ttk.Entry(root, width=5, style="TEntry")
entry1.pack(side=tk.LEFT, padx=10, pady=11)
 
entry2 = ttk.Entry(root, width=5, style="TEntry")
entry2.pack(side=tk.LEFT, padx=10, pady=11)

# Add the buttons for each operation
add_button = tk.Button(root, text="+", command=add , bg= "yellow" , fg= "black")
add_button.pack(side=tk.LEFT, padx=30, pady=30)

subtract_button = tk.Button(root, text="-", command=subtract , bg= "yellow" , fg= "black")
subtract_button.pack(side=tk.LEFT, padx=30, pady=30)

multiply_button = tk.Button(root, text="*", command=multiply , bg= "yellow" , fg= "black")
multiply_button.pack(side=tk.LEFT, padx=30, pady=30)

divide_button = tk.Button(root, text="/", command=divide , bg= "yellow" , fg= "black")
divide_button.pack(side=tk.LEFT, padx=30, pady=30)

# Add a label to display the result
result_label = ttk.Label(root, text="Result", style="TLabel")
result_label.pack(side=tk.TOP, pady=55)

# Start the GUI
animate()
root.mainloop()
