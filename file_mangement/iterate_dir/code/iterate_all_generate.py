'''
this code is create a generator which get data from a file in a subfolder. The subfolder indicates the label
of that datapoint
You run into this when in the speech recognition project on Kaggle.

''' 
import os
def train_generator():
  for subdir, folders, files, in os.walk("../data"):
      for file in files:
          with open(subdir+os.sep+file, 'r') as f:
              _, folder = os.path.split(subdir)
              yield (f.readline().strip("\n"),folder)

train_generator = train_generator()

for data in train_generator:
    print data
