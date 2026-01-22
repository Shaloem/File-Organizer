#Necessary Libraries
import os #interacts with file sys
import shutil #moves files btw directories

FILE_CATEGORIES = {
    "Images" : [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos" : [".mp4", ".mkv", ".flv", ".avi", ".mov"],
    "Documents" : [".pdf", ".docx", ".doc", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Audio" : [".mp3", ".wav", ".aac", ".flac"],
    "Archives" : [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Data" : [".csv", ".json", ".xml"],
    "Others" : []
}

#Organizing Function
def organize_files(directory):
    """Organizes files in the given directory by their file types."""
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return
    
    #Creating folders for each category if they don't exist
    for category in FILE_CATEGORIES:
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)

    #Moving files to appropriate folders
    for fileName in os.listdir(directory):
        file_path = os.path.join(directory, fileName)

        #Skipping if it is a directory
        if os.path.isdir(file_path):
            continue

        #Checking file extension and move to the corresponding folder.
        file_moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if any(fileName.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(directory, category, fileName))
                file_moved = True
                break

        #Moving to "others" if no Match
        if not file_moved:
            shutil.move(file_path, os.path.join(directory, "Others", fileName))
    print(f"Files in '{directory}' have been organized successfully!")

#User Input
directory_to_organize = input("Enter the directory path to organize: ")
organize_files(directory_to_organize)