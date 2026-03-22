# 📁 Python File Organizer

A simple Python script that organizes files in a specified directory into categorized folders based on file extensions.
This project demonstrates basic file system operations using Python’s built-in modules.

---

## Features

* Organizes files into predefined categories:

  * Images
  * Videos
  * Documents
  * Audio
  * Archives
  * Data
  * Others
* Automatically creates folders if they do not exist
* Case-insensitive file extension matching
* Skips subdirectories
* Moves unmatched files into an `Others` folder
* Command-line based interaction

---

## File Categories

**Images**
`.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`

**Videos**
`.mp4`, `.mkv`, `.flv`, `.avi`, `.mov`

**Documents**
`.pdf`, `.docx`, `.doc`, `.txt`, `.ppt`, `.pptx`, `.xls`, `.xlsx`

**Audio**
`.mp3`, `.wav`, `.aac`, `.flac`

**Archives**
`.zip`, `.rar`, `.7z`, `.tar`, `.gz`

**Data**
`.csv`, `.json`, `.xml`

Any other file type is moved to the **Others** folder.

---

## Requirements

* Python 3.x
* No external libraries required

---

## Usage

1. Download or clone the repository.
2. Run the script:

```bash
python file_organizer.py
```

3. When prompted, enter the full path of the directory you want to organize.
4. Press Enter to start the process.

---

## How It Works

* Verifies the provided path is a valid directory.
* Creates category folders inside the target directory.
* Scans all files in the main directory.
* Moves each file into its matching category folder.
* Displays a success message after completion.

---

## Notes

* Files are moved, not copied.
* Subdirectories are not processed.
* If a file with the same name already exists in a destination folder, an error may occur.
* Always verify the directory path before running the script.
