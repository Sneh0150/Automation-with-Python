import os
from datetime import datetime

print("Hello Automation! start my First Automated Task!!..")


Folder_name = "Automate_folder"
if not os.path.exists(Folder_name):
    os.mkdir(Folder_name)
    print(f"Folder named {Folder_name} created Successfully! ")

file_path = os.path.join(Folder_name,'My_Text.txt')
with open(file_path,mode="w") as f:
    f.write("This is my first text file created through python automation Script! \n")
    f.write(f'Timestamp: {datetime.now()}\n')

print(f'The My_text has been created successfully in {Folder_name} folder with a custom message.')        
