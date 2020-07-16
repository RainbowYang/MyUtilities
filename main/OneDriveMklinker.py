"""
使用mklink，将一个文件夹连接(mklink /J)到OneDrive目录下
"""

from util.util import *

# 默认为当前用户文件夹
userFolder = os.path.expanduser('~')
OneDriveFolder = userFolder + "/OneDrive"

askFolderUntilCancelFor(
    lambda target:
    mklink(OneDriveFolder + "/" + target.split("/")[-1], target)
)
