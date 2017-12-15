from keras.utils import to_categorical
import numpy as np
labels = ['1','2','3']
print(to_categorical(labels))


labels = [1,2,3]
print(to_categorical(labels,num_classes=5))

print(np.eye(8)[labels])

