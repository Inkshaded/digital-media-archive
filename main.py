import tkinter as tk
from tkinter import messagebox, filedialog
from ui.ui_start import ArchiveUI
from controller_interface import FileSelector, Storage

# TODO: Seperate ArchiveApp controller from main.py
class ArchiveApp:
    """ Controller to connect GUI to file operations """
    def __init__(self, root: tk.Tk, selector: FileSelector, storage: Storage):
        self.root = root
        self.selector = selector
        self.storage = storage
        self.gui = ArchiveUI(root, app_logic=self)

    def upload_file(self):
        file_path = self.selector.select_file()
        if not file_path:
            messagebox.showinfo("No Selection", "No file was selected.")
            return
        
        #Update view
        self.gui.update_selected_file(file_path)

        try:
            saved_path = self.storage.save(file_path, dest_root="archive")
            messagebox.showinfo("Success", f"Archived file to:\n{saved_path}")
        except RuntimeError as e:
            messagebox.showerror("Error", str(e))

def main():
    from implementations.tk_file_selector import TkFileSelector
    from implementations.local_storage import LocalStorage

    root = tk.Tk()
    ArchiveApp(root, selector=TkFileSelector(), storage=LocalStorage())
    root.mainloop()

if __name__ == "__main__":
    main()