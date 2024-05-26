import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display input and output
entry = tk.Entry(root, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Create buttons and add functionality
for (text, row, column) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, padx=40, pady=20, command=button_equal)
    elif text == "C":
        btn = tk.Button(root, text=text, padx=40, pady=20, command=button_clear)
    else:
        btn = tk.Button(root, text=text, padx=40, pady=20, command=lambda t=text: button_click(t))
    btn.grid(row=row, column=column)

root.mainloop()
