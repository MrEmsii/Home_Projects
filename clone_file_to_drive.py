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

now = datetime.datetime.now()
f = []
for mypath in mypath_list:
    for (dirpath, dirnames, filenames) in os.walk(drive_src + mypath):
        
        if mypath != "Wzór":
            f.extend(dirnames)
        break
    f.remove("Wzór")
    
    print(f)

    for dirnames in f:
        # if not os.path.exists(drive_dest + mypath + "/" + dirnames):
        #     os.mkdir(drive_dest + mypath + "/" + dirnames)
        #     print("Folder %s created!" % dirnames)
        if os.path.exists(drive_src + mypath + "/" + dirnames + "/G-Code"):    
            shutil.copytree(drive_src + mypath + "/" + dirnames + "/G-Code", drive_dest + mypath + "/" + dirnames, ignore=shutil.ignore_patterns('*.ini', 'tmp*'), dirs_exist_ok=True)
            print("Folder %s created!" % dirnames)
             
    f = []
now = abs(datetime.datetime.now() - now)
now = now.seconds
print(f"Czas obliczeń: {now} sekund!")

print("STOP")