# 🧮 GUI Calculator using Python (Tkinter)
# Created by Aditi 💫

from tkinter import *

# Create main window
root = Tk()
root.title("Simple Calculator")
root.geometry("350x500")
root.config(bg="#222831")

# Entry box (display)
entry = Entry(root, width=20, font=('Arial', 24), border=5, relief=RIDGE, justify='right', bg="#eeeeee")
entry.pack(pady=20)

# Function to handle button clicks
def click(button_text):
    current = entry.get()
    if button_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, END)
            entry.insert(END, result)
        except:
            entry.delete(0, END)
            entry.insert(END, "Error")
    elif button_text == "C":
        entry.delete(0, END)
    else:
        entry.insert(END, button_text)

# Button frame
frame = Frame(root, bg="#222831")
frame.pack()

# Buttons layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'C', '+'],
    ['=']
]

# Create buttons dynamically
for row in buttons:
    row_frame = Frame(frame, bg="#222831")
    row_frame.pack()
    for btn_text in row:
        Button(
            row_frame,
            text=btn_text,
            width=5,
            height=2,
            font=('Arial', 18, 'bold'),
            bg="#00adb5",
            fg="white",
            activebackground="#393e46",
            activeforeground="white",
            relief=RAISED,
            bd=2,
            command=lambda t=btn_text: click(t)
        ).pack(side=LEFT, padx=5, pady=5)

# Footer label
Label(root, text="Made with ❤️ by Aditi", bg="#222831", fg="#00adb5", font=('Arial', 10, 'italic')).pack(pady=10)

root.mainloop()
