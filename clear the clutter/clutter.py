# a simple program to clear the clutter

import os

files = os.listdir("clear the clutter")
i=0
for file in files:
    if file.endswith(".jpg"):
        print(file)
        os.rename(f"clear the clutter/{file}", f"clear the clutter/{i}.jpg")
        i=i+1