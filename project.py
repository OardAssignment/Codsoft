import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        update_status()

def update_task():
    selected_task = listbox.curselection()
    if selected_task:
        selected_index = selected_task[0]
        updated_task = entry.get()
        if updated_task:
            listbox.delete(selected_index)
            listbox.insert(selected_index, updated_task)
            entry.delete(0, tk.END)
            update_status()
        else:
            messagebox.showwarning("Update Error", "Please enter a valid task to update.")
    else:
        messagebox.showwarning("Update Error", "Select a task to update.")

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
        update_status()
    else:
        messagebox.showwarning("Delete Error", "Select a task to delete.")

def update_status():
    task_count.set(f"Total Tasks: {listbox.size()}")

# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Create an entry widget for adding/updating tasks
entry = tk.Entry(window)
entry.pack(pady=10)

# Create a button to add tasks
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack()

# Create a button to update tasks
update_button = tk.Button(window, text="Update Task", command=update_task)
update_button.pack()
update_button.bbox()
# Create a listbox to display tasks
listbox = tk.Listbox(window)
listbox.pack()

# Create a button to remove tasks
remove_button = tk.Button(window, text="Remove Task", command=remove_task)
remove_button.pack()

# Create a label to show task count
task_count = tk.StringVar()
task_count_label = tk.Label(window, textvariable=task_count)
task_count_label.pack()

# Start the Tkinter main loop
window.mainloop()
