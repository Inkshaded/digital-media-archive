import tkinter as tk
from tkinter import filedialog

# TODO: Seperate browseFiles function from ui
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = (("Text files", "*.txt*"), 
                                                        ("All files", "*.*")))

class ArchiveUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Media Archiving System")
        self.root.geometry("900x700")

        # ~~~ (In Window) Title ~~~
        tk.Label(root, text="Digital Media Archiving System", font=("Arial", 18, "bold")).pack(pady=10)

        tk.Button(root, text="Upload Files", command=browseFiles).pack()
