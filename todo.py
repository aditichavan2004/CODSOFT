import tkinter as tk
from tkinter import messagebox, Scrollbar, RIGHT, Y

tasks = []

# ----------------- Functions ----------------- #
def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append({"task": task, "done": False})
        task_entry.delete(0, tk.END)
        update_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def mark_done():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = True
        update_tasks()
    else:
        messagebox.showwarning("Warning", "Select a task to mark done!")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_tasks()
    else:
        messagebox.showwarning("Warning", "Select a task to delete!")

def update_tasks():
    task_listbox.delete(0, tk.END)
    for t in tasks:
        status = "✅ Done" if t["done"] else "⏳ Pending"
        task_listbox.insert(tk.END, f"{t['task']} - {status}")
        index = task_listbox.size() - 1  # Correct index for itemconfig
        color = "#198754" if t["done"] else "#fd7e14"  # Green = done, Orange = pending
        task_listbox.itemconfig(index, fg=color)

# ----------------- GUI Setup ----------------- #
root = tk.Tk()
root.title("📝 To-Do List App")
root.geometry("500x480")
root.resizable(False, False)
root.configure(bg="#f0f4f8")  # light soft background

# Heading
heading = tk.Label(root, text="To-Do List", font=("Helvetica", 22, "bold"), bg="#f0f4f8", fg="#333")
heading.pack(pady=15)

# Task Entry Frame
task_frame = tk.Frame(root, bg="#ffffff", bd=0)
task_frame.pack(pady=10, padx=20, fill="x")

task_entry = tk.Entry(task_frame, font=("Helvetica", 13), bd=2, relief="groove")
task_entry.pack(side=tk.LEFT, fill="x", expand=True, padx=10, pady=10)

# Function to create buttons with hover effect
def create_rounded_button(parent, text, bg_color, hover_color, command):
    btn = tk.Button(parent, text=text, bg=bg_color, fg="white",
                    font=("Helvetica", 12, "bold"), bd=0, padx=15, pady=7, cursor="hand2", command=command,
                    activebackground=hover_color, relief="flat")
    btn.bind("<Enter>", lambda e: btn.config(bg=hover_color))
    btn.bind("<Leave>", lambda e: btn.config(bg=bg_color))
    return btn

add_button = create_rounded_button(task_frame, "Add Task", "#0d6efd", "#339af0", add_task)
add_button.pack(side=tk.LEFT, padx=5)

# Task Listbox with Scrollbar
list_frame = tk.Frame(root, bg="#f0f4f8")
list_frame.pack(padx=20, pady=10, fill="both", expand=True)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=RIGHT, fill=Y)

task_listbox = tk.Listbox(list_frame, font=("Helvetica", 12), bd=2, relief="groove",
                          selectbackground="#b3d7ff", activestyle="none", yscrollcommand=scrollbar.set)
task_listbox.pack(fill="both", expand=True)
scrollbar.config(command=task_listbox.yview)

# Action Buttons Frame
buttons_frame = tk.Frame(root, bg="#f0f4f8")
buttons_frame.pack(pady=15)

mark_done_button = create_rounded_button(buttons_frame, "Mark Done", "#198754", "#28a745", mark_done)
mark_done_button.pack(side=tk.LEFT, padx=10)

delete_button = create_rounded_button(buttons_frame, "Delete Task", "#dc3545", "#f44336", delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
