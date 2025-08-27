import tkinter as tk
from tkinter import messagebox
from functools import partial
import commands

def handle_delete(id,app):
    commands.delete_task(id)
    show_all_tasks_frame(app) #print(id)


def submit_task(title,app):
    if not title:
        messagebox.showerror(
            title="Add Task",
            message="cannot add empty task!",
            parent=app
        )
    else:
        commands.save_task({"title":title})
        show_all_tasks_frame(app)

    commands.save_task({"title":title})
    show_add_task_frame(app)

def show_add_task_frame(app):
    frame =tk.Frame(master =app)
    frame.grid( row =0, column=0, sticky="nsew", padx=10, pady=10)

    label= tk.Label(master=frame, text="what do you want to do?")
    label.grid()
    entry = tk.Entry(master =frame)
    entry.grid()
    btn =tk.Button( master=frame, text="submit",command=lambda:submit_task(entry.get(),app))
    btn.grid()

    frame.tkraise()

def show_all_tasks_frame(app):
    frame =tk.Frame(master=app)
    frame.grid( row=0, column=0, sticky="nsew",padx=10, pady=10)

    tasks= commands.get_tasks().to_list()
    for task in tasks:
        checkbtn = tk.Checkbutton(master=frame, text =task["title"])
        checkbtn.grid( row=tasks.index(task),column=0)

        edit_btn =tk.Button(
            master=frame,
            text="Edit"
        )
        edit_btn.grid(row=tasks.index(task),column=1)

        btn =tk.Button(master=frame, text="Delete",command=partial(handle_delete, task["_id"],app) )
        btn.grid(row=tasks.index(task), column=2)

    btn =tk.Button(master = frame, text="Add Task",command=lambda: show_add_task_frame(app))
    btn.grid(row=len(tasks) + 5, column= 1)

    frame.tkraise()