import os
import shutil
from tqdm import tqdm

def move_files_to_parent(directory):
    # List to store file paths for moving
    files_to_move = []

    # Check if the provided directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Walk through the directory to gather files to move
    for root, dirs, files in os.walk(directory):
        # Check if the current directory is one of the specified directories
        if os.path.basename(root) in ["flow_x", "flow_y", "img"]:
            parent_dir = os.path.dirname(root)
            for file in files:
                # Construct full file path and store it with the destination
                file_path = os.path.join(root, file)
                destination = os.path.join(parent_dir, file)
                files_to_move.append((file_path, destination))

    # Move files with progress bar
    for file_path, destination in tqdm(files_to_move, desc="Moving files", unit="file"):
        shutil.move(file_path, destination)

if __name__ == "__main__":
    dir_path = input("Enter the path to the directory: ")
    move_files_to_parent(dir_path)
