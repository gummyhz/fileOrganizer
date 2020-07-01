import os
import shutil

## File Organizer
##  def include( )
##  Advanced Concepts in Python
##  June 2020

#dictionary of file categories and file extensions
DIRECTORIES = {
    "Web": [".html5", ".html", ".htm", ".xhtml", ".css", ".webarchive", ".php", ".yaml"],
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", ".heif", ".jfif"],
    "Photoshop": [".psd"],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
    "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", "pptx", ".csv"],
    "Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
    "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "Plain Text": [".txt", ".in", ".out", ".key", ".md"],
    "PDF": [".pdf"],
    "Code": [".py", ".java", ".RData", ".Rhistory", ".cpp", ".o"],
    "Shortcuts": [".lnk", ".url"],
    "Configuration": [".ini", ".msi", ".apk", ".crdownload"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]
}

#The path of the directory to be sorted
#edit this to where you placed your test-file folder
path = 'C:\\Users\\Rebecca\\github\\fileOrganizer\\test-file'

list_ = os.listdir(path)    # Creates a list with the filenames in the directory

for file_ in list_:                         # goes through every file in the directory
    name, ext = os.path.splitext(file_)     # 1. Create variables name and ext and set them to the file_'s name and extention

    if ext == '':           # Checks if there is no extension
        continue            # If the extension variable is empty, moves onto the next iteration

    for directory in DIRECTORIES:               # 2. Loop through DIRECTORIES
        if ext in DIRECTORIES[directory]:           # 3. If the extension is in one of the lists
            print("ext:", ext, "directory list: ", DIRECTORIES[directory])
            if directory in os.listdir(path):       # 4. Check if the key is a folder in the current directory already
                shutil.move(file_, directory)       # 5. If the key is already a folder in the directory, move the file into that directory using shutil.move

            else:                                   # 6. If the folder is not in the current directory already,
                os.chdir(path)
                os.makedirs(directory)             # create the folder
                shutil.move(file_, directory)       # 7. Move the file into that directory using shutil.move

        else:                                   # 8. Else, continue to the next iteration
            continue
