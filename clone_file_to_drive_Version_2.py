# Author: Emsii 
# Date: 20.03.2024
# https://github.com/EmsiiDiss
#
# A program designed for copying folders and files from one location to another, 
# specifically targeting folders containing G-code files. 
# This tool is essential for private applications.

import datetime
import os
import shutil
import threading

drive_dest = "E:/"
drive_src = "G:/.shortcut-targets-by-id/1NV5-iDSWkzujlti1hy-S4DMccnFwygvG/DYSK/"
mypath_list = ["Druk_3D", "Projekty_Inne"]

liter = 0
sum = 0
f = []

def list_folders(mypath):
    for (dirpath, dirnames, filenames) in os.walk(drive_src + mypath):
        f.extend(dirnames)
        break
    f.remove("Wzór")
    f.sort()
    return f

def copy_file(mypath, dirnames):
    global sum
    src = drive_src + mypath + "/" + dirnames + "/G-Code"
    dest = drive_dest + mypath + "/" + dirnames
    
    
    if (not os.path.exists(dest)) or (os.stat(src).st_mtime - os.stat(dest).st_mtime > 1):
        shutil.copytree(src, dest, ignore=shutil.ignore_patterns('*.ini', '.tmp*'), dirs_exist_ok=True, copy_function=shutil.copy2)
        string_in = str(round(sum/len(f)*100 + liter, 2)) + "%"
        sum += 1
        print(f"{string_in.ljust(10)} | Folder {dirnames} copied!")

def copy():
    threads = []
    for mypath in mypath_list:
        f = list_folders(mypath)
        for dirnames in f:
            if os.path.exists(drive_src + mypath + "/" + dirnames + "/G-Code"):
                t1 = threading.Thread(target=copy_file, args=(mypath, dirnames,))
                t1.start()
                threads.append(t1)

    # Joining all threads to wait for their completion
    for thread in threads:
        thread.join()


def delete_empty_folders(root = drive_dest):
   for dirpath, dirnames, filenames in os.walk(root, topdown=False):
      for dirname in dirnames:
         full_path = os.path.join(dirpath, dirname)
         if not os.listdir(full_path): 
            os.rmdir(full_path)

try:
    now = datetime.datetime.now()
    copy()
    delete_empty_folders()

except KeyboardInterrupt:
    print("Break")

finally:
    print(f"{"100%".ljust(10)} | All folders copied!")
    now = abs(datetime.datetime.now() - now)
    now = now.seconds
    print(f"Czas kopiowania: {now} sekund!")
