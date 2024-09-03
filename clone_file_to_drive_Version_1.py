# Author: MrEmsii 
# Date: 20.03.2024
# https://github.com/MrEmsii
#
# A program designed for copying folders and files from one location to another, 
# specifically targeting folders containing G-code files. 
# This tool is essential for private applications.

import datetime
import os, shutil
from pathlib import Path
from humanize import naturalsize

drive_dest = "E:/"
drive_src = "G:/.shortcut-targets-by-id/1NV5-iDSWkzujlti1hy-S4DMccnFwygvG/DYSK/"
mypath_list = ["Druk_3D","Projekty_Inne"]


def get_size(path):
    size = 0
    for file_ in Path(path).rglob('*'):
        size += file_.stat().st_size
    return naturalsize(size)

def copy():
    liter = 0
    sum = 0
    f = []
    for mypath in mypath_list:
        for (dirpath, dirnames, filenames) in os.walk(drive_src + mypath):
            f.extend(dirnames)
            break
        f.remove("Wzór")
        f.sort()

        for dirnames in f:
            if os.path.exists(drive_src + mypath + "/" + dirnames + "/G-Code"):
                src = drive_src + mypath + "/" + dirnames + "/G-Code"
                dest = drive_dest + mypath + "/" + dirnames
                liter = (f.index(dirnames)+1)/(len(f)+0.1)*100/len(mypath_list)
                string_in = str(round(sum + liter, 2)) + "%"
                if (not os.path.exists(dest)) or (os.stat(src).st_mtime - os.stat(dest).st_mtime > 1) or ((get_size(src) != get_size(dest)) and get_size(src) != "244 Bytes"):
                    shutil.copytree(src, dest, ignore=shutil.ignore_patterns('*.ini', '.tmp*'), dirs_exist_ok=True, copy_function = shutil.copy2)
                    print(f"{string_in.ljust(10)} | Folder {dirnames} copied!")
        sum = liter
        f = []



def delete_empty_folders(root = drive_dest):
   for dirpath, dirnames, filenames in os.walk(root, topdown=False):
      for dirname in dirnames:
         full_path = os.path.join(dirpath, dirname)
         if not os.listdir(full_path): 
            os.rmdir(full_path)


try:
    now = datetime.datetime.now()
    print(f"{"0.00%".ljust(10)} | Starting copy files!")
    copy()
    delete_empty_folders()

except KeyboardInterrupt:
    print("Break")
finally:
    print(f"{"100%".ljust(10)} | All folders copied!")
    now = abs(datetime.datetime.now() - now)
    now = now.seconds
    print(f"Czas kopiowania: {now} sekund!")    