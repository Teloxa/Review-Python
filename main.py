import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Task Manager")
        self.root.geometry("400x450")

        # 01 Initial array of tasks
        self.tasks = ["Study Python", "Exercise", "Read book"]

        # --- UI ELEMENTS ---
        
        # Title
        self.label = tk.Label(root, text="My Task List", font=("Arial", 14, "bold"))
        self.label.pack(pady=10)

        # Input field to add new tasks
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=5)

        # Buttons Frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        # Add Button (corresponds to .append)
        self.add_button = tk.Button(button_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        # Delete Button (corresponds to .pop)
        self.delete_button = tk.Button(button_frame, text="Remove Selected", command=self.remove_task)
        self.delete_button.grid(row=0, column=1, padx=5)

        # Listbox to display tasks
        self.tasks_listbox = tk.Listbox(root, width=40, height=10)
        self.tasks_listbox.pack(pady=10, padx=20)

        # Initialize the list display
        self.update_listbox()

    def update_listbox(self):
        """Clears and re-populates the listbox from the array."""
        self.tasks_listbox.delete(0, tk.END)  # Clear current view
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

    def add_task(self):
        """Adds a new task using the .append() method."""
        task_text = self.task_entry.get()
        if task_text != "":
            self.tasks.append(task_text)  # Array logic
            self.update_listbox()         # UI update
            self.task_entry.delete(0, tk.END) # Clear input
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        """Removes the selected task using the .pop() logic."""
        try:
            # Get the index of the selected item
            selected_index = self.tasks_listbox.curselection()[0]
            # Remove from our array
            removed = self.tasks.pop(selected_index)
            # Refresh UI
            self.update_listbox()
            messagebox.showinfo("Done", f"Task '{removed}' completed!")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()