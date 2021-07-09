import os
import time

DAYS = 2    # Maximal age of time stay, older will be deleted
FOLDERS =   [
                "C:\TRASH",
                "C:\HLAM"
            ]
TOTAL_DELETED_SIZE = 0  # TOTAL DELETED SIZE OF ALL FILES
TOTAL_DELETED_FILE = 0  # TOTAL DELETED FILES
TOTAL_DELETED_DIRS = 0  # TOTAL DELETED EMPTY FOLDERS

nowTime = time.time()               # Get current time in seconds
ageTime = nowTime - 60*60*24*DAYS   # Minux DAYS in SECONDS


def delete_old_files(folder):
    """Delete files older then X DAYS"""
    global TOTAL_DELETED_FILE
    global TOTAL_DELETED_SIZE
    for path, dirs, files in os.walk(folder):
        for file in files:
            fileName = os.path.join(path, file)     #get full Path to file
            fileTime = os.path.getmtime(fileName)
            if fileTime < ageTime:
                sizeFile = os.path.getsize(fileName)
                TOTAL_DELETED_SIZE += sizeFile      #Count sum of all free space
                TOTAL_DELETED_FILE += 1             #Count number of deleted files
                print("deleting file: " + str(fileName))
                os.remove(fileName)                 #Delete file

def delete_empty_dir(folder):
    global TOTAL_DELETED_DIRS
    empty_folder_this_run = 0
    for path, dirs, files in os.walk(folder):
        if (not dirs) and (not files):
            TOTAL_DELETED_DIRS += 1
            print("Deleting Empty dir " + str(path))
            os.rmdir(path)
    if empty_folder_this_run > 0:
        delete_empty_dir(folder)
#=======================MAIN========================

starttime = time.asctime()

for folder in FOLDERS:
    delete_old_files(folder)    # Delete old files
    delete_empty_dir(folder)    # Delete empty folders

finishtime = time.asctime()

print("------------------------------")
print("START TIME: "                    + str(starttime))
print("Total Deleted Size: "            + str(int(TOTAL_DELETED_SIZE/1024/1024)) + "MB")
print("Total Deleted file: "            + str(TOTAL_DELETED_FILE) + " items")
print("Total Deleted Empty folders: "   + str(TOTAL_DELETED_DIRS) + " items")
print("FINISH TIME: "                   + str(finishtime))
print("----------------EOF---------------------")
