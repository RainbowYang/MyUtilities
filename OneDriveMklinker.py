"""
使用mklink，将一个文件夹连接(mklink /J)到OneDrive目录下
"""

import tkinter as tk
from tkinter import filedialog
import os

# 默认为当前用户文件夹
userFolder = os.path.expanduser('~')
OneDriveFolder = userFolder + "/OneDrive"

root = tk.Tk()
root.withdraw()

while True:
    targetFolder = filedialog.askdirectory()
    folderName = targetFolder.split("/")[-1]

    if len(str(folderName)) == 0:
        break

    link = OneDriveFolder + "/" + folderName
    os.system('mklink /J "' + link + '" "' + targetFolder + '"')
    print(targetFolder, "has been linked to", link)
