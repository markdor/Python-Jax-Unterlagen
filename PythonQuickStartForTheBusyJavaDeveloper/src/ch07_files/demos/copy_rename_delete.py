import os

print(os.listdir())


import shutil

shutil.copy('personenliste.py', "copy_of_personenliste.py")
print(os.listdir())

os.rename('copy_of_personenliste.py', 'to-be-deleted.py')
print(os.listdir())

os.remove('to-be-deleted.py')
print(os.listdir())


os.mkdir("new_and_empty")
os.rmdir('new_and_empty')
print(os.listdir())

os.mkdir("dir-to-be-deleted")
open("dir-to-be-deleted/to-be-deleted-1.txt", "x")
print(os.listdir())
#os.rmdir('dir-to-be-deleted')

shutil.rmtree("dir-to-be-deleted")
print(os.listdir())