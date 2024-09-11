import os
import shutil
import time

# Define the target path where the folder will be created
target_path = r"C:/Users/phand/miniconda3/Lib/site-packages"

# Define the source folder to be copied
source_folder = 'mediapipe'

# Combine the target path with the source folder to create the full destination path
destination_path = os.path.join(target_path, source_folder)

# Create the target folder if it does not exist
if not os.path.exists(target_path):
    os.makedirs(target_path)
    print(f"Created directory: {target_path}")

# Copy the source folder to the destination path
if os.path.exists(source_folder):
    shutil.copytree(source_folder, destination_path, dirs_exist_ok=True)
    print(f"Copied '{source_folder}' to '{destination_path}'")
else:
    print(f"Source folder '{source_folder}' does not exist in the current directory.")

time.sleep(3)
