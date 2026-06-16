#File Organizer

A Python based file organization tool that automatically sorts files into different folders based on their extensions.

## 🚀 Features

* Automatically organizes files by file extension.
* Creates destination folders if they do not already exist.
* Moves files into their respective folders.
* Supports multiple file types.
* Handles invalid paths and common exceptions gracefully.

## 🛠️ Built With

* Python 3
* os module
* shutil module

## 📁 Supported File Types

| File Extension | Destination Folder |
| -------------- | ------------------ |
| .jpg, .png | Images             |
|  .pdf      | PDFs               |
|  .mp3      | Music              |
|  .mp4      | Videos             |
|  .txt      | TextFiles          |
|  .py       | PythonFiles        |

## 📋 Project Workflow

1. Accept a folder path from the user.
2. Read all files in the folder.
3. Check whether each item is a file or a folder.
4. Identify the file extension.
5. Map the extension to the appropriate folder using a dictionary.
6. Create the destination folder if it does not exist.
7. Move the file into the correct folder.

## ▶️ How to Run

1. Clone this repository.
2. Open the project in Python.
3. Run the script.
4. Enter the folder path when prompted.

```bash
python file_organizer.py
```

## 📸 Example

### Before

text
TestFolder/
│
├── photo.jpg
├── notes.pdf
├── song.mp3
├── code.py
└── hello.txt


### After

text
TestFolder/
│
├── Images/
│     └── photo.jpg
│
├── PDFs/
│     └── notes.pdf
│
├── Music/
│     └── song.mp3
│
├── PythonFiles/
│     └── code.py
│
└── TextFiles/
      └── hello.txt


## 📚 Concepts Used

* File Handling
* Dictionaries
* Loops
* Exception Handling
* os.listdir()
* os.path.join()
* os.path.isfile()
* os.path.splitext()
* os.path.exists()
* os.mkdir()
* shutil.move()

## Author

**Lakkakula Charan Teja**

This project was built to practice Python file handling, dictionaries, exception handling, and automation concepts through a real-world project.
