import os
import shutil
from pathlib import Path

# Define the source directory to organize
SOURCE_DIR = Path.home() / 'Downloads'  # Change as needed

# Define the target directories and their corresponding file extensions
SORTING_MAP = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac'],
    'Archives': ['.zip', '.tar', '.gz', '.rar'],
    'Applications': ['.exe', '.msi', '.dmg', '.apk'],
    'Scripts': ['.py', '.js', '.sh', '.bat'],
    'Others': []
}

def organize_files():
    for item in SOURCE_DIR.iterdir():
        if item.is_file():
            file_ext = item.suffix.lower()
            moved = False
            for folder, extensions in SORTING_MAP.items():
                if file_ext in extensions:
                    target_folder = Path.home() / folder
                    target_folder.mkdir(exist_ok=True)
                    shutil.move(str(item), str(target_folder / item.name))
                    print(f'Moved: {item.name} to {folder}/')
                    moved = True
                    break
            if not moved:
                target_folder = Path.home() / 'Others'
                target_folder.mkdir(exist_ok=True)
                shutil.move(str(item), str(target_folder / item.name))
                print(f'Moved: {item.name} to Others/')

if __name__ == '__main__':
    organize_files()

