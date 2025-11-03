import os


def save_uploaded_file(file_path, destination_folder="archive"):
    try:
        os.makedirs(destination_folder, exist_ok=True)
        filename = os.path.basename(file_path)
        dest_path = os.path.join(destination_folder, filename)
        with open(file_path, 'rb') as src, open(dest_path, 'wb') as dst:
            dst.write(src.read())
            
        return dest_path
    
    except Exception as e:
        raise RuntimeError(f"Failed to copy {file_path}: {e}")