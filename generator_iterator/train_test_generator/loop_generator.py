'''
This code is a simpiled version for generating training batches when training a model

1. This is an endless generator
2. In each iteration in the while loop, all the batches is went through
3. Before each iteration in the while loop, the file_paths is re_generated
   This is to tackle the case where the number of datapoints is different for each type

'''
import random    
import os
import glob

from PIL import Image as pil_image
epoch_size = 2
size_total = 2*2
batch_size = 1
def get_file_paths(train_dir):
    file_paths = []
    for folder in os.listdir(train_dir):
        file_path = glob.glob(train_dir + os.sep + folder + "/*")
        random.shuffle(file_path)
        file_paths += file_path[:epoch_size]
    random.shuffle(file_paths) # shuffle is critical
    return file_paths
    
def tr_te_ge(train_dir):    
    while True:    
        l = get_file_paths(train_dir)
        for start in range(0,size_total,2):    
            batch = []              
            end = min(start+2,size_total)            
            for i in range(start,end,1):    
                batch.append(l[i])    
            yield batch    
                     
tr_ge=tr_te_ge("./train_dir")     
print(next(tr_ge))    
print(next(tr_ge))    
print(next(tr_ge))
print(next(tr_ge))                                                              
