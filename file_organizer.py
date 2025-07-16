import os
import shutil
from pathlib import Path
from datetime import datetime

def organize_files(folder_path):
    folder = Path(folder_path)
    counter = {}

    for file in folder.iterdir():
        if file.is_file():
            ext = file.suffix.lower().strip('.')
            ctime = datetime.fromtimestamp(file.stat().st_ctime)
            date_str = ctime.strftime('%Y%m%d')
            month_str = ctime.strftime('%Y-%m')

            file_type = categorize_file(ext)
            new_folder = folder / file_type / month_str
            new_folder.mkdir(parents=True, exist_ok=True)

            counter_key = f"{file_type}_{date_str}"
            counter[counter_key] = counter.get(counter_key, 0) + 1
            new_name = f"{file_type}_{date_str}_{counter[counter_key]:03d}{file.suffix}"

            shutil.move(str(file), new_folder / new_name)
            print(f"Moved {file.name} → {new_folder}/{new_name}")

def categorize_file(ext):
    image_exts = {'jpg', 'jpeg', 'png', 'gif'}
    doc_exts = {'pdf', 'docx', 'txt'}
    code_exts = {'py', 'js', 'html', 'css'}

    if ext in image_exts:
        return 'images'
    elif ext in doc_exts:
        return 'documents'
    elif ext in code_exts:
        return 'code'
    else:
        return 'others'

# Example usage
organize_files("your target file")
