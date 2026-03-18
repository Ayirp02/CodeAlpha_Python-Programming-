import os
import shutil

# 👉 Step 1: Give your folder paths
source_folder = r"C:\Users\NEELESH\Downloads"
destination_folder = r"C:\Users\NEELESH\Pictures\JPG_Files"

# 👉 Step 2: Create destination folder if not exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 👉 Step 3: Move JPG files
for file in os.listdir(source_folder):
    if file.endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)
        print(f"Moved: {file}")

print("✅ All JPG files moved successfully!")
