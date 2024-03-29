# Author: Emsii 
# Date: 20.03.2024
# https://github.com/EmsiiDiss
#
# A program designed for copying folders and files from one location to another, 
# specifically targeting folders containing G-code files. 
# This tool is essential for private applications.

import datetime
import os, shutil

drive_dest = "E:/"
drive_src = "G:/.shortcut-targets-by-id/1NV5-iDSWkzujlti1hy-S4DMccnFwygvG/DYSK/"
mypath_list = ["Druk_3D","Projekty_Inne"]

liter = 0
sum = 0
f = []
now = datetime.datetime.now()

for mypath in mypath_list:
    for (dirpath, dirnames, filenames) in os.walk(drive_src + mypath):
        f.extend(dirnames)
        break

    f.remove("Wzór")

    for dirnames in f:
        if os.path.exists(drive_src + mypath + "/" + dirnames + "/G-Code"):
            src = drive_src + mypath + "/" + dirnames + "/G-Code"
            dest = drive_dest + mypath + "/" + dirnames
            if (not os.path.exists(dest)) or (os.stat(src).st_mtime - os.stat(dest).st_mtime > 1) :
                shutil.copytree(src, dest, ignore=shutil.ignore_patterns('*.ini', '.tmp*'), dirs_exist_ok=True, copy_function = shutil.copy2)
        liter = (f.index(dirnames)+1)/(len(f)+0.1)*100/len(mypath_list)
        string_in = str(round(sum + liter, 2)) + "%"
        print(string_in, (20-len(string_in)) * " ", "Folder %s copied!" % dirnames)
    sum = liter
    f = []
print("100%", 16*" ", "All Folders copied!")
now = abs(datetime.datetime.now() - now)
now = now.seconds
print(f"Czas kopiowania: {now} sekund!")
