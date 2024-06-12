import tkinter as tk
from tkinter import messagebox

def click(event):
    current = display.get()
    button_text = event.widget.cget("text")
    
    if button_text == "=":
        try:
            result = eval(current)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
    elif button_text == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, button_text)

root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.SUNKEN)
display.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

buttons_frame = tk.Frame(root)
buttons_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

i = 0
for btn_text in buttons:
    button = tk.Button(buttons_frame, text=btn_text, font=("Arial", 20), bd=5, relief=tk.RAISED)
    button.grid(row=i//4, column=i%4, sticky="nsew")
    button.bind("<Button-1>", click)
    i += 1

for i in range(4):
    buttons_frame.grid_columnconfigure(i, weight=1)
    buttons_frame.grid_rowconfigure(i, weight=1)

root.mainloop()

