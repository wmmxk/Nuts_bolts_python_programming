from _init_paths import *
import os
from data_gen.data_generator import *
tr_generator = data_generator(os.path.join(project_dir,"data"))
img, label = next(tr_generator)
print(label)
