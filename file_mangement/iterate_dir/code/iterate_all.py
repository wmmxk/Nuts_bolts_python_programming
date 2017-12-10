'''
this code is loop through the files in each subfolders in one 
1. The results of os.walk("../data") is 
  ('../data', ['sub_folder2', 'sub_folder1'], [])
  ('../data/sub_folder2', [], ['test2.dat', 'test1.txt'])
  ('../data/sub_folder1', [], ['test2.dat', 'test1.txt'])
  
  each is a tuple of three elements: subdir, folders, files.
  for the first tuple, the files is empty. So when you loop through the files list in each tuple, the first one does nothing.
2. use a tuple to pass multiple extension to endswith function. regular expression does not work
''' 
import os

for f in os.walk("../data"):
    print f

for subdir, folders, files, in os.walk("../data"):
    print folders
    for file in files:
        if file.endswith(("txt","dat")):
            print os.path.join(subdir,file)
