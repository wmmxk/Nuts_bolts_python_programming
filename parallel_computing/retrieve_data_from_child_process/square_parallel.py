import sys
from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing import cpu_count

n = int(sys.argv[1])
mylist = list(range(n))

num_cpu = cpu_count()
size_chunk = int(len(mylist)/num_cpu)
print("----size_chunk-----", size_chunk)

def square_chunk(idx, queue):
    global mylist
    start = idx * size_chunk
    end = min(len(mylist), (idx+1)*size_chunk)
    for i in range(start, end):
        queue.put(mylist[i]**2)

res = []
queues = [Queue() for i in range(num_cpu)]
args = [(i,q) for i, q in enumerate(queues)]
jobs = [Process(target=square_chunk, args = (a)) for a in args]

for j in jobs:
    j.start()

for i,q in enumerate(queues):
    while not q.empty():
        res.append(q.get())

for j in jobs:
    j.join()




if len(res)<10:
   print("elements in results {} ".format(res))
else:
   print("elements in results {} ".format(res[:10]))
