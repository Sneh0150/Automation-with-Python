from SendInvite import send_invites
import os
import shutil

Employees =  ["Reema", "Akash", "Riya", "Mohit", "Sujata"]

# Folder which we are creating here Personalized Message folder
Folder_name = "Invites_Msg"

# Create a folder if not exist
if not os.path.exists(Folder_name):
    os.mkdir(Folder_name)

# Source Template file
source_template ="Template_Msg.txt"

# For every employee
for name in Employees:
    msg = send_invites(name)
    # for each employee create its own file
    template_disct = os.path.join(Folder_name,f"{name}_message.txt")
    shutil.copy(source_template,template_disct)
    
    # Appeneding my message

    with open(template_disct,mode="a") as f:
        f.write('\n')
        f.write(msg)

print("all message are created Successfully !!! ")