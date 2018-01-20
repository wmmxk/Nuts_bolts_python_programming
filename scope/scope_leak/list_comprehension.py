'''
The snippet demonstrated two points:
    list comprehension has scope leakage: after the list comprehension, the i is still there. but for a generator expression, that is not the case

    But in python 3, there is no scope leakage even in list comprehension

'''
l = [i for i in range(3)]
print('i is {}'.format(i))

g = (i for i in range(6))

print('i is {}'.format(i))
