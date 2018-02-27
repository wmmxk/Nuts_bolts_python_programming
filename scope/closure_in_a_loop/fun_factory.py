def make_fun(var):
    def f():
        print(var)
    return f

funcs = []
for i in range(4):
    funcs.append(make_fun(var=i))

for f in funcs:
    f()
