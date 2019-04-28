
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
    __repr__ = __str__

    def __call__(self):
        print('My name is %s.' % self.name)

if __name__ == '__main__':
    print(Chain().Status.user.time.list)
    s = Chain()
    print(s())