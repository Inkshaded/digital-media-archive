import os
from tkinter import filedialog, messagebox


def select_file():
    path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("All Files", "*.*")]
    )
    return path if path else None

def save_uploaded_file(file_path, destination_folder="archive"):
    try:
        os.makedirs(destination_folder, exist_ok=True)
        filename = os.path.basename(file_path)
        dest_path = os.path.join(destination_folder, filename)
        with open(file_path, 'rb') as src, open(dest_path, 'wb') as dst:
            dst.write(src.read())
        return dest_path
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to copy {file_path}:\n{e}")
        return None