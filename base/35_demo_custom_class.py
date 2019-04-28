
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration
        return self.a

    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a

class Someone(object):
    def __init__(self):
        self.name = 'kepler'

    def __getattr__(self, item):
        if item == 'store':
            return 'this is store'

if __name__ == '__main__':
    print(Student('kepler'))
    for n in Fib():
        print(n)
    print(Fib()[3])
    a = Someone()
    print(a.store)