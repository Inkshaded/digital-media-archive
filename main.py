import tkinter as tk
from tkinter import messagebox
from ui.ui_start import ArchiveUI
from utility import file_utility

# TODO: Seperate ArchiveApp controller from main.py
class ArchiveApp:
    """ Controller to connect GUI to file operations """
    def __init__(self, root: tk.Tk):
        self.root = root
        self.gui = ArchiveUI(root, app_logic=self)

    def upload_file(self):
        file_path = file_utility.select_file()
        if not file_path:
            messagebox.showinfo("No Selection", "No file was selected.")
            return
        
        self.gui.update_selected_file(file_path)

        saved_path = file_utility.save_uploaded_file(file_path, destination_folder="archive")
        if saved_path:
            messagebox.showinfo("Success", f"Archived file to:\n{saved_path}")

def main():
    root = tk.Tk()
    ArchiveApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()