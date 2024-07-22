import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        save_tasks()
        task_entry.delete(0, tk.END)


def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_task_list()
        save_tasks()


def cross_off_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task = tasks[selected_task_index[0]]
        if not task.startswith("✓ "):
            tasks[selected_task_index[0]] = "✓ " + task
            update_task_list()
            save_tasks()


def uncross_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task = tasks[selected_task_index[0]]
        if task.startswith("✓ "):
            tasks[selected_task_index[0]] = task[2:]
            update_task_list()
            save_tasks()


def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)


def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks.extend(line.strip() for line in file.readlines())
            update_task_list()
    except FileNotFoundError:
        pass


# an empty list to store the to-do list items.
tasks = []

# to create tkinter window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x500")

# Load background image using Pillow
bg_image = Image.open("wallpaper.png")
bg_photo = ImageTk.PhotoImage(bg_image)

# Create and set up the GUI components with background image
background_label = tk.Label(root, image=bg_photo)
background_label.place(relwidth=1, relheight=1)

# Entry, Buttons, and Listbox
task_entry = tk.Entry(root, font=('Helvetica', 14), bd=2, relief=tk.FLAT)
add_button = ttk.Button(root, text="Add Task", command=add_task, style="TButton")
task_listbox = tk.Listbox(root, font=('Helvetica', 16), selectmode=tk.SINGLE, bd=2, relief=tk.FLAT, height=10)
delete_button = ttk.Button(root, text="Delete Task", command=delete_task, style="TButton")
cross_off_button = ttk.Button(root, text="Cross Off Task", command=cross_off_task, style="TButton")
uncross_button = ttk.Button(root, text="Uncross Task", command=uncross_task, style="TButton")

# Packing widgets with padding and spacing
task_entry.pack(pady=(20, 5))
add_button.pack(pady=5)
task_listbox.pack(pady=10, padx=20)
delete_button.pack(pady=5)
cross_off_button.pack(pady=5)
uncross_button.pack(pady=5)

# Use the 'clam' theme for ttk widgets on macOS
root.tk_setPalette(background='#ececec')
style = ttk.Style(root)
style.theme_use('clam')

# Load tasks from task.txt
load_tasks()

root.mainloop()
