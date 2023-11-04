import tkinter as tk
import math

def on_click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "sqrt":
        entry.insert(tk.END, "math.sqrt(")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculadora Científica")

entry = tk.Entry(root, font=("Helvetica", 20))
entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=10, ipadx=8, ipady=8)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "/", "C",
    "4", "5", "6", "*", "sqrt",
    "1", "2", "3", "-", "**",
    "0", ".", "=", "+", "pi",
]

row, col = 1, 0

for button in buttons:
    button_obj = tk.Button(button_frame, text=button, font=("Helvetica", 15), width=5, height=2)
    button_obj.grid(row=row, column=col)
    button_obj.bind("<Button-1>", on_click)
    col += 1
    if col > 4:
        col = 0
        row += 1

root.mainloop()