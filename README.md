# 📁 Python File Organizer

## 📌 Overview
This project is a Python-based file organization script that automatically sorts files in a given directory into categorized folders based on their file extensions.

It helps keep directories clean and organized by grouping files such as images, documents, videos, audio files, and more into separate folders.

---

## 🛠 Features
- Automatically detects file types using extensions
- Organizes files into predefined categories:
  - Images
  - Videos
  - Documents
  - Audio
  - Archives
  - Data
  - Others
- Creates category folders if they do not already exist
- Skips directories to avoid errors
- Simple and easy-to-use command-line interface

---

## 🧰 Technologies Used
- Python 3
- `os` module (file system operations)
- `shutil` module (file moving operations)

---

## 🚀 How to Run the Project

1. Make sure you have Python 3 installed on your system.
2. Download the `file_organizer.py` script from the repository.
3. Open your terminal and run the script:

```
python file_organizer.py
```

4. When prompted, paste the path to the folder you want to organize (e.g., your Downloads folder).
5. Hit Enter on your keyboard to start organizing the files.
6. The script will automatically organize any new files in that folder.
