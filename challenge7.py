### 📅 Challenge 7: os Library
##* Write a function to create a directory if it doesn’t already exist.
##* List all files in the directory, including subdirectories, using recursion.
##* Function signature: `create_and_list_dir(dir_path: str) -> list[str]`.

import os

def create_and_list_dir(dir_path: str) -> list[str]:
    os.makedirs(dir_path, exist_ok=True)
    
    def list_files_recursive(current_path: str) -> list[str]:
        files = []
        for entry in os.listdir(current_path):
            entry_path = os.path.join(current_path, entry)
            if os.path.isdir(entry_path):
                files.extend(list_files_recursive(entry_path))
            else:
                files.append(entry_path)
        return files
    
    return list_files_recursive(dir_path)

## Test
if __name__ == "__main__":
    directory_path = "C:/Users/Asus/Desktop/software-team-training-path/second_week/Challenges Simon Ocampo/example_directory-challenge7"
    files = create_and_list_dir(directory_path)
    print(f"Files '{directory_path}':", files)