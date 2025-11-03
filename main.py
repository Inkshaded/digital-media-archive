import tkinter as tk
from tkinter import messagebox, filedialog
from ui.ui_start import ArchiveUI
from utility import file_utility

def select_file():
    path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("All Files", "*.*")]
    )
    return path if path else None

# TODO: Seperate ArchiveApp controller from main.py
class ArchiveApp:
    """ Controller to connect GUI to file operations """
    def __init__(self, root: tk.Tk):
        self.root = root
        self.gui = ArchiveUI(root, app_logic=self)

    def upload_file(self):
        file_path = select_file()
        if not file_path:
            messagebox.showinfo("No Selection", "No file was selected.")
            return
        
        #Update view
        self.gui.update_selected_file(file_path)

        #File-saving logic (managed by file_utility)
        try:
            saved_path = file_utility.save_uploaded_file(file_path, destination_folder="archive")
            messagebox.showinfo("Success", f"Archived file to:\n{saved_path}")
        except RuntimeError as e:
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    ArchiveApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()