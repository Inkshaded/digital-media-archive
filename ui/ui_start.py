import tkinter as tk
from tkinter import messagebox

class ArchiveUI:
    def __init__(self, root, app_logic):
        self.root = root
        self.app_logic = app_logic

        self.root.title("Digital Media Archiving System")
        self.root.geometry("900x700")

        # ~~~ Widgets ~~~
        # -- Title --
        self.title_label = tk.Label(root, text="Digital Media Archiving System", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=10)

        # -- Upload Button --
        self.upload_button = tk.Button(root, text="Upload Files", command=self.app_logic.upload_file)
        self.upload_button.pack()

        # -- Upload Listbox --
        self.file_listbox = tk.Listbox(
            root,
            width=50,
            height=1,
            selectmode=tk.SINGLE
        )
        self.file_listbox.pack(pady=12, padx=10, fill="x")

        # --- Helpers for controller ---
    def update_selected_file(self, file_path: str):
        """Replace the list contents with a single selected file path."""
        self.file_listbox.delete(0, tk.END)
        self.file_listbox.insert(tk.END, file_path)
