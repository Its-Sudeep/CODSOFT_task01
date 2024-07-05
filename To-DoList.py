import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("500x450+400+100")
root.resizable(False, False)

task_list = []

def add_task():
    task = task_entry.get()
    task_entry.delete(0, tk.END)
    
    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"{task}\n")
        task_list.append(task)
        listbox.insert(tk.END, task)

def delete_task():
    selected_index = listbox.curselection()
    if selected_index:
        task = listbox.get(selected_index)
        task_list.remove(task)
        with open("tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        listbox.delete(selected_index)

def open_task_file():
    try:
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task.strip():
                task_list.append(task.strip())
                listbox.insert(tk.END, task.strip())
    except:
        with open('tasklist.txt', 'w') as file:
            pass


top_frame = tk.Frame(root, bg="#32405b", height=100)
top_frame.pack(fill=tk.X)

heading = tk.Label(top_frame, text="To-Do List", font="Arial 24 bold", fg="white", bg="#32405b")
heading.pack(pady=20)


input_frame = tk.Frame(root, width=450, height=50, bg="white")
input_frame.pack(pady=10)

task_entry = tk.Entry(input_frame, width=33, font="Arial 15")
task_entry.grid(row=0, column=0, padx=10)
task_entry.focus()

add_button = tk.Button(input_frame, text="Add Task", font="Arial 14", width=10, bg="#5a95ff", fg="#fff", bd=0, command=add_task)
add_button.grid(row=0, column=1, padx=10)


task_frame = tk.Frame(root, bd=3, width=450, height=250, bg="#32405b")
task_frame.pack(pady=20)

listbox = tk.Listbox(task_frame, font=('Arial', 12), width=40, height=12, bg="#32405b", fg="white", selectbackground="#5a95ff")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)

scrollbar = tk.Scrollbar(task_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


delete_button = tk.Button(root, text="Delete Task", font="Arial 14", width=10, bg="#ff5a5a", fg="#fff", bd=0, command=delete_task)
delete_button.pack(pady=(0, 10))


open_task_file()

root.mainloop()
