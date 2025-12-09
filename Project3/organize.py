from pathlib import Path
import os
import shutil

def organize_file(Folder_Name):

    folder = Path(Folder_Name)

    # Creating Sub folders
    image_folder = folder/"Images"
    text_folder = folder/"Text_Files"
    Csv_folder = folder/"CSV_Files"

    # To cerate folder is not present
    image_folder.mkdir(exist_ok=True)
    text_folder.mkdir(exist_ok=True)
    Csv_folder.mkdir(exist_ok=True)

    image_ext = [".jpg", ".jpeg", ".png", ".gif", ".avif"]
    text_ext = [".txt", ".docx"]
    csv_ext = [".csv,.xlsx"]

    # Looping through all files in the folder

    for file in folder.iterdir():
        if file.is_file():
            extension = file.suffix.lower()

            if extension in image_ext:
                shutil.move(str(file),str(image_folder/file.name))
            elif extension in text_ext:
                shutil.move(str(file),str(text_folder/file.name))
            else:
                shutil.move(str(file),str(Csv_folder/file.name))        

print("File orgainzed sucessfully!!!.")


organize_file("DownloadFiles")