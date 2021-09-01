# 2. Write a Python program to get the size, permissions, owner, device, created, last modified, and last accessed date
# time of a specified path.
import os
import time

l = os.listdir(os.getcwd())

for elemento in l:
    if os.path.isfile(os.path.join(os.getcwd(),elemento)):
        print("Archivo: ",elemento)
        print("Size: ", os.path.getsize(os.path.join(os.getcwd(),elemento)), "bytes")
        print("Permissions: ", oct(os.stat(os.path.join(os.getcwd(),elemento)).st_mode))
        print("Device: ", os.stat(os.path.join(os.getcwd(),elemento)).st_dev)
        print("Owner: ", os.stat(os.path.join(os.getcwd(),elemento)).st_uid)
        print("Creation: ", time.ctime(os.path.getctime(os.path.join(os.getcwd(),elemento))))
        print("Modification: ", time.ctime(os.path.getmtime(os.path.join(os.getcwd(),elemento))))
        print("Last Access: ", time.ctime(os.path.getatime(os.path.join(os.getcwd(),elemento))))
        print("==\n")
#size
#print(o)

#permissions

#owner

#device

#created datetime

#last modified

#last accessed

