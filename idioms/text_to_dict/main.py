class Person:
    def __init__(self, name = ''):
        self.name = name


if __name__ == '__main__':
    f = open('people.dat','r')
    people = []
    for l in f.readlines():
        people.append(Person())
        lsp = l.strip().split(',')
        p = []

        for i in lsp:
            p.append(i.split('='))
        people[-1].__dict__ = dict(p)

    for p in people:
        print(p.__dict__)
