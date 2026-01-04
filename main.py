import tkinter as tk # Standard library for Graphical User Interfaces (GUI)
from tkinter import messagebox # Module for pop-up alert boxes

class TaskManagerApp:
    """
    A Class representing the Task Manager application.
    Using a class helps keep the 'data' (the list) and the 'actions' (the functions) 
    organized together in one object.
    """
    def __init__(self, root):
        # 'root' is the main window provided by Tkinter
        self.root = root
        self.root.title("Python Task Manager") # Sets the window title
        self.root.geometry("400x450") # Sets initial size (Width x Height)

        # 01 DATA STORAGE (The "State" of our app)
        # We use a standard Python List to store our strings.
        self.tasks = ["Study Python", "Exercise", "Read book"]

        # --- UI ELEMENTS (The "View" of our app) ---
        
        # Label: A non-editable text element for titles or instructions
        self.label = tk.Label(root, text="My Task List", font=("Arial", 14, "bold"))
        self.label.pack(pady=10) # .pack() places the element and adds 10px vertical padding

        # Entry: A single-line text field where the user types new tasks
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=5)

        # Frame: An invisible container used to group other widgets (like buttons) together
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        # Buttons: Executed when 'command' is triggered (clicked)
        # 'grid' is used inside the frame to place buttons side-by-side (columns)
        self.add_button = tk.Button(button_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.delete_button = tk.Button(button_frame, text="Remove Selected", command=self.remove_task)
        self.delete_button.grid(row=0, column=1, padx=5)

        # Listbox: A scrollable list that displays our array items visually
        self.tasks_listbox = tk.Listbox(root, width=40, height=10)
        self.tasks_listbox.pack(pady=10, padx=20)

        # Update the Listbox immediately so we see the initial tasks
        self.update_listbox()

    def update_listbox(self):
        """
        Synchronizes the UI (Listbox) with the Data (List).
        Whenever the array changes, we clear the visual list and redraw it.
        """
        self.tasks_listbox.delete(0, tk.END)  # Remove all items from index 0 to the End
        for task in self.tasks:
            # tk.END tells Python to insert the new item at the very bottom
            self.tasks_listbox.insert(tk.END, task)

    def add_task(self):
        """Logic for adding a task."""
        task_text = self.task_entry.get() # .get() retrieves what the user typed
        
        if task_text != "": # Validation: Don't add empty tasks
            self.tasks.append(task_text)  # 02 Array logic: Add to the end of the list
            self.update_listbox()         # Refresh the visual display
            self.task_entry.delete(0, tk.END) # Clear the input box for the next task
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        """Logic for deleting a selected task."""
        try:
            # curselection() returns a tuple of indexes. [0] gets the first one selected.
            selected_index = self.tasks_listbox.curselection()[0]
            
            # .pop(index) removes the item from the array at that specific position
            removed = self.tasks.pop(selected_index)
            
            # Refresh the UI to reflect the removal
            self.update_listbox()
            messagebox.showinfo("Done", f"Task '{removed}' completed!")
        except IndexError:
            # This handles the error if the user clicks 'Remove' without selecting anything
            messagebox.showwarning("Warning", "Please select a task from the list first.")

# --- APPLICATION ENTRY POINT ---
if __name__ == "__main__":
    root = tk.Tk() # Create the base Tkinter engine
    app = TaskManagerApp(root) # Instantiate our class
    root.mainloop() # Run the "Event Loop" (keeps the window open and listening for clicks)