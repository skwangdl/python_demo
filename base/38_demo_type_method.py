
def fn(self, name='kepler'):
    print('hello, %s.' %name)

Hello = type('Hello', (object,), dict(hello=fn))

if __name__ == '__main__':
    h = Hello()
    h.hello()