'''
This snippet is to show how to utilize the property of or operator to
address the exception for the first iteration


'''
import random
perfs = []
for i in range(5):
   perf = random.uniform(0,1)
   if i==0 or perfs[-1] < perf:
       perfs.append(perf)

print(perfs)
