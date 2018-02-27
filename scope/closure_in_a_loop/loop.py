funcs = []
# the function defined closures over variable i but not the value of i
# When the function is run, the value of i is equal to 3

for i in range(4):
    def f():
        print i
    funcs.append(f)

for f in funcs:
    f()
