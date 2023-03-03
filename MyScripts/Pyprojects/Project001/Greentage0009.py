#Pathlib basics

from pathlib import Path
import shutil

home = Path.home()
#directory = r"C:\your\directoy"

#Creating a directory called "Main Folder" in the root directory.
myfolder = home/"Main Folder"
myfolder.mkdir()
img_dir = myfolder/"Images"
img_dir.mkdir()

#To check if a folder or a file exists..
#myfolder.exists()

#Inside Main Folder, create three files: 'file1.txt', 'file2.txt' and 'image1.png'.
files = ('file1.txt', 'file2.txt', 'image1.png')
for file in files:
    (myfolder/"{}".format(file)).touch()

#Move "image1.png" to img_dir directory.
directory = img_dir/ "image1.png"
(myfolder/"image1.png").replace(directory)

#Deleting "image1.png" in Images folder/directory.
(img_dir/"image1.png").unlink()

#Delete Main Folder directory.
shutil.rmtree(myfolder)

