import sys
n = int(sys.argv[1])
mylist = list(range(n))

res = []
for i in mylist:
    res.append(i*i)
print("----%d number of elements in results"%(len(res)))
