import os         # Library to interact with Operating System (files/folders)

# Path of target folder where automation need to be done.
folder_path = r"C:\Users\YourName\Desktop\TestFolder"   =

print("📁 Scanning folder for files...\n")

# List all files present in folder
for file in os.listdir(folder_path):
    print("Found File:", file)  # Print file names one by one

# Creating new folder named 'Text_Files' if not created
new_folder = os.path.join(folder_path, "Text_Files")

if not os.path.exists(new_folder):
    os.mkdir(new_folder)
    print("\n📂 'Text_Files' folder created successfully!")
else:
    print("\n📂 'Text_Files' folder already exists.")

print("\n📦 Moving .txt files to Text_Files folder...")

# Moving all .txt file to the target folder
for file in os.listdir(folder_path):
    if file.endswith(".txt"):     # Checking on the based of extension
        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(new_folder, file)

        os.rename(old_path, new_path)   # Moving the file
        print(f"➡ {file} moved!")

print("\n🎉 Automation Complete!")
print("All text files are now organized in 'Text_Files' folder.")
