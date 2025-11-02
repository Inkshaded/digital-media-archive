import tkinter as tk


class ArchiveUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Media Archiving System")
        self.root.geometry("900x700")

        # ~~~ (In Window) Title ~~~
        tk.Label(root, text="Digital Media Archiver", font=("Arial", 18, "bold")).pack(pady=10)