import os
import shutil


def remove_if_exists(path):
    if os.path.exists(path):
        os.remove(path)


# clean-up
if os.path.exists("new_and_empty"):
    shutil.rmtree("new_and_empty")
if os.path.exists("another-dir"):
    shutil.rmtree("another-dir")
remove_if_exists("image-info.txt")
remove_if_exists("response-data.json")
remove_if_exists("mypic.png")

os.mkdir("new_and_empty")
os.mkdir('another-dir')
print(os.listdir())

open("another-dir/file-1.txt", "x")
open("another-dir/file-2.txt", "x")
open("image-info.txt", "x")
open("response-data.json", "x")
open("mypic.png", "x")

print(os.listdir())
