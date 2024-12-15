import tkinter as tk
from tkinter import messagebox

class TaskTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Task Tracker")
        
        self.tasks = []

        # Create and place widgets
        self.title_label = tk.Label(root, text="Daily Task Tracker", font=("Arial", 18))
        self.title_label.pack(pady=10)

        self.task_entry = tk.Entry(root, width=40, font=("Arial", 14))
        self.task_entry.pack(pady=10)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task, font=("Arial", 14))
        self.add_task_button.pack(pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 14))
        self.task_listbox.pack(pady=10)

        self.complete_task_button = tk.Button(root, text="Complete Task", command=self.complete_task, font=("Arial", 14))
        self.complete_task_button.pack(pady=10)
        
        self.show_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.show_tasks()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks.pop(selected_task_index[0])
            self.show_tasks()
            messagebox.showinfo("Task Completed", f"Great job completing: {task}")
        else:
            messagebox.showwarning("Warning", "You must select a task to complete.")

    def show_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskTrackerApp(root)
    root.mainloop()
