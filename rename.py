import os

directory_path = filepath

def rename_files_and_folders(root):
    for directory, subdirectories, files in os.walk(root, topdown=False):
        for name in files + subdirectories:
            if '+' in name:
                new_name = name.replace('+', 'と')
                src = os.path.join(directory, name)
                dst = os.path.join(directory, new_name)
                os.rename(src, dst)  
                
rename_files_and_folders(directory_path)