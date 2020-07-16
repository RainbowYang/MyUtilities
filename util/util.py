import os
import tkinter as tk
from tkinter import filedialog
from zipfile import *


def mklink(link, target):
    os.system('mklink /J "' + link + '" "' + target + '"')


def zipFolder(target):
    z = ZipFile(target + '.zip', 'w', ZIP_DEFLATED)
    for now_dir, _, files in os.walk(target):
        # 在zip文件中的地址，也就是相对于被压缩文件夹的地址
        inner_dir = now_dir.replace(target, '')
        # 根目录无需分隔符，子目录需要分隔符
        inner_dir = '' if inner_dir == '' else inner_dir + os.sep
        for filename in files:
            z.write(now_dir + os.sep + filename, inner_dir + filename)
    z.close()
    print('压缩成功')


def askFolderUntilCancelFor(func):
    # 消除主界面
    tk.Tk().withdraw()

    while True:
        targetFolder = filedialog.askdirectory()
        if len(str(targetFolder)) == 0:
            break
        func(targetFolder)
