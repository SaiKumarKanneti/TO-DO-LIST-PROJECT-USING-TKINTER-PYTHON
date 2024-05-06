
# TITLE - To-Do List application
# NAME - SAI KUMAR
# EMAIL - SK54541N@PACE.EDU

import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = task_entry.get()  # Take the task from the input field.
    if task:  # Check if the task is not empty
        task_listbox.insert(tk.END, task)  # Add the task to the listbox
        task_entry.delete(0, tk.END)  # Clear the entry field
    else:
        messagebox.showwarning("Warning", "Please enter a task.")  # Show a warning if the task is empty

# Function to remove a selected task from the list
def remove_task():
    try:
        task_index = task_listbox.curselection()[0]  # Obtain the specified task's index.
        task_listbox.delete(task_index)  # Take the chosen task out of the listbox.
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")  # Show a warning if no task is selected

# Function to clear the entire task list
def clear_list():
    task_listbox.delete(0, tk.END)  # Clear all tasks from the listbox

# Create the main window
root = tk.Tk()
root.title("To-Do List")


# Entry field for adding tasks
task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=6, pady=6)

# Button to add a task
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.grid(row=0, column=1, padx=6, pady=6)

# Button to remove a task
remove_button = tk.Button(root, text="Remove Task", width=20, command=remove_task)
remove_button.grid(row=1, column=0, padx=6, pady=6)

# Button to clear the entire list
clear_button = tk.Button(root, text="Clear List", width=20, command=clear_list)
clear_button.grid(row=1, column=1, padx=6, pady=6)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=60)
task_listbox.grid(row=2, column=0, columnspan=3, padx=6, pady=6)

# Start the Tkinter event loop
root.mainloop()
