import sys
n = int(sys.argv[1])
mylist = list(range(n))

res = []
for i in mylist:
    res.append(i*i)
if len(res)<10:
   print("elements in results {} ".format(res))

else:
   print("elements in results {} ".format(res[:10]))
