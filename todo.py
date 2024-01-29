import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List App")

        self.tasks = []
        self.completed_tasks = set()

        # Create widgets
        self.task_entry = tk.Entry(root, width=30)
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)

        # Pack widgets
        self.task_entry.pack(pady=10)
        self.add_button.pack()
        self.task_listbox.pack(pady=10)
        self.delete_button.pack()
        self.complete_button.pack()

        # Bind double click event to task_listbox
        self.task_listbox.bind('<Double-1>', self.complete_task)

        # Populate the task list
        self.update_task_list()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.tasks[selected_index[0]]
            self.tasks.remove(selected_task)
            self.completed_tasks.discard(selected_task)
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def complete_task(self, event=None):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.tasks[selected_index[0]]
            if selected_task not in self.completed_tasks:
                self.completed_tasks.add(selected_task)
            else:
                self.completed_tasks.remove(selected_task)
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            if task in self.completed_tasks:
                self.task_listbox.insert(tk.END, f"[✓] {task}")
            else:
                self.task_listbox.insert(tk.END, f"[] {task}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

