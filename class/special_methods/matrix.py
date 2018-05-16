class matrix:
    def __getitem__(self, pos):
        x,y = pos
        return "fetching %s, %s" % (x, y)

m = matrix()
tuples = [(1,2),(3,4),(5,6)]
for i in tuples:
    print(m[i])
