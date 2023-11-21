import tkinter as tk
from tkinter import filedialog
import subprocess

class ScriptRunnerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dummy Data Generator")

        self.create_ui()

    def create_ui(self):
        # Create buttons for each script
        button_generate_emails = tk.Button(self.root, text="Generate Dummy Emails", command=self.run_generate_emails)
        button_generate_first_names = tk.Button(self.root, text="Generate Dummy First Names", command=self.run_generate_first_names)
        button_generate_last_names = tk.Button(self.root, text="Generate Dummy Last Names", command=self.run_generate_last_names)
        button_generate_phones = tk.Button(self.root, text="Generate Dummy Phone Numbers", command=self.run_generate_phones)

        # Arrange buttons in a grid
        button_generate_emails.grid(row=0, column=0, padx=10, pady=10)
        button_generate_first_names.grid(row=0, column=1, padx=10, pady=10)
        button_generate_last_names.grid(row=0, column=2, padx=10, pady=10)
        button_generate_phones.grid(row=0, column=3, padx=10, pady=10)

    def run_generate_emails(self):
        self.run_script("generate_dummy_emails.py")

    def run_generate_first_names(self):
        self.run_script("generate_dummy_first_names.py")

    def run_generate_last_names(self):
        self.run_script("generate_dummy_last_names.py")

    def run_generate_phones(self):
        self.run_script("generate_dummy_phones.py")

    def run_script(self, script_name):
        script_path = filedialog.askopenfilename(filetypes=[("Python Scripts", "*.py")], title="Select Script")
        if script_path:
            subprocess.run(["python", script_path])

if __name__ == "__main__":
    root = tk.Tk()
    app = ScriptRunnerApp(root)
    root.mainloop()
