import os          # Used for file and folder operations
import shutil      # Used for moving files

# Take folder path from the user
path = input("Please enter a Folder Path:\n")

# Dictionary to map file extensions to folder names
file_types = {
    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "PDFs",
    ".mp3": "Music",
    ".mp4": "Videos",
    ".txt": "TextFiles",
    ".py": "PythonFiles"
}

try:

    # Check whether the given path is a valid folder
    if os.path.isdir(path):

        # Get all files and folders inside the given path
        files = os.listdir(path)

    else:
        print("Path does not exist")
        exit()

    # Loop through every item in the folder
    for file in files:

        # Create the complete path of the current item
        file_path = os.path.join(path, file)

        # Check whether the current item is a file
        if os.path.isfile(file_path):

            # Split file name and extension
            name, ext = os.path.splitext(file)

            # Convert extension to lowercase
            ext = ext.lower()

            # Check if extension exists in dictionary
            if ext in file_types:

                # Get destination folder name from dictionary
                folder_name = file_types[ext]

                print(f"{file} should go to {folder_name}")

                # Create full path of destination folder
                new_folder_path = os.path.join(path, folder_name)

                # Create folder if it does not exist
                if not os.path.exists(new_folder_path):

                    os.mkdir(new_folder_path)
                    print(f"{folder_name} created successfully")

                else:
                    print(f"{folder_name} already exists")

                # Create destination path including file name
                destination = os.path.join(new_folder_path, file)

                # Move file from old location to new location
                shutil.move(file_path, destination)

                print(f"{file} moved successfully\n")

            else:
                # Extension not found in dictionary
                print(f"{file} : Unknown file type\n")

        else:
            # Skip folders
            print(f"{file} is a folder")

# Handle the case when user enters a file path instead of folder path
except NotADirectoryError:
    print("You entered a file path. Please enter a folder path.")

# Handle invalid folder path
except FileNotFoundError:
    print("Folder not found.")

# Handle permission issues
except PermissionError:
    print("Permission denied.")

# Handle any unexpected errors
except Exception as e:
    print("Error:", e)
