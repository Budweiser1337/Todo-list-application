import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List App")
        self.root.geometry("400x300")  # Set initial window size

        self.tasks = []
        self.completed_tasks = set()

        # Create frames
        self.input_frame = tk.Frame(root)
        self.list_frame = tk.Frame(root)
        self.button_frame = tk.Frame(root)

        # Create widgets
        self.task_label = tk.Label(self.input_frame, text="Enter Task:")
        self.task_entry = tk.Entry(self.input_frame, width=30)
        self.add_button = tk.Button(self.input_frame, text="Add Task", command=self.add_task)

        self.task_listbox = tk.Listbox(self.list_frame, selectmode=tk.SINGLE, height=10, width=40)
        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.complete_button = tk.Button(self.button_frame, text="Complete Task", command=self.complete_task)

        # Pack frames
        self.input_frame.pack(pady=10)
        self.list_frame.pack(pady=10)
        self.button_frame.pack(pady=10)

        # Pack widgets
        self.task_label.grid(row=0, column=0, padx=5)
        self.task_entry.grid(row=0, column=1, padx=5)
        self.add_button.grid(row=0, column=2, padx=5)

        self.task_listbox.pack()

        self.delete_button.grid(row=0, column=0, padx=5)
        self.complete_button.grid(row=0, column=1, padx=5)

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

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            if 0 <= selected_index < len(self.tasks):
                selected_task = self.tasks.pop(selected_index)
                self.completed_tasks.discard(selected_task)
                self.update_task_list()
            else:
                messagebox.showwarning("Warning", "Invalid selection.")
        else:
           messagebox.showwarning("Warning", "Please select a task to delete.")


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
