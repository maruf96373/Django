import sqlite3
from tkinter import Tk, Label, Entry, Button, Listbox, END

# SQLite Database setup
def setup_database():
    """Create the database and tasks table if not exists."""
    conn = sqlite3.connect("todo_list.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_task():
    """Add a new task to the database."""
    task = entry_task.get()
    if task.strip():  # Ensure task is not empty
        conn = sqlite3.connect("todo_list.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
        conn.close()
        entry_task.delete(0, END)
        load_tasks()

def delete_task():
    """Delete the selected task from the database."""
    selected_task = listbox_tasks.get(listbox_tasks.curselection())
    conn = sqlite3.connect("todo_list.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE task = ?", (selected_task,))
    conn.commit()
    conn.close()
    load_tasks()

def load_tasks():
    """Load tasks from the database into the Listbox."""
    listbox_tasks.delete(0, END)
    conn = sqlite3.connect("todo_list.db")
    cursor = conn.cursor()
    cursor.execute("SELECT task FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    for task in tasks:
        listbox_tasks.insert(END, task[0])

# GUI Setup
setup_database()

root = Tk()
root.title("To-Do List")
root.geometry("300x400")

# Task Entry
label_task = Label(root, text="Enter a new task:")
label_task.pack(pady=5)
entry_task = Entry(root, width=25)
entry_task.pack(pady=5)

# Buttons
button_add = Button(root, text="Add Task", command=add_task)
button_add.pack(pady=5)
button_delete = Button(root, text="Delete Task", command=delete_task)
button_delete.pack(pady=5)

# Task List
listbox_tasks = Listbox(root, width=35, height=15)
listbox_tasks.pack(pady=10)

# Load tasks at startup
load_tasks()

# Run the application
root.mainloop()
