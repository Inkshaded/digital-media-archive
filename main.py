import tkinter as tk
from tkinter import filedialog
from ui.ui_start import ArchiveUI

def main():
    root = tk.Tk()
    app = ArchiveUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()